from flask import Blueprint, request, jsonify, current_app
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_mail import Message
import os
import bcrypt
import random
import jwt
import datetime
from pathlib import Path

# Load environment variables
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

auth_bp = Blueprint("auth", __name__)

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

users = db["users"]
otp_collection = db["otp_codes"]
courses = db["courses"]
tasks = db["tasks"]
quizzes = db["quizzes"]

# ================= REGISTER =================
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    full_name = data.get("fullName")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not all([full_name, email, password, role]):
        return jsonify({
            "message": "All fields are required"
        }), 400

    existing_user = users.find_one({"email": email})

    if existing_user:
        return jsonify({
            "message": "Account already exists"
        }), 409

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    users.insert_one({
        "fullName": full_name,
        "email": email,
        "password": hashed_password,
        "role": role
    })

    return jsonify({
        "message": "Registration successful"
    }), 201


# ================= LOGIN =================
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = users.find_one({"email": email})

    if not user:
        return jsonify({
            "message": "Account does not exist"
        }), 404

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        user["password"]
    ):
        return jsonify({
            "message": "Invalid password"
        }), 401

    # Generate OTP
    otp = str(random.randint(100000, 999999))

    # Remove old OTPs
    otp_collection.delete_many({"email": email})

    # Store new OTP
    otp_collection.insert_one({
        "email": email,
        "otp": otp
    })

    print(f"OTP for {email}: {otp}")

    # Send OTP via Brevo
    msg = Message(
        subject="Lumina Login OTP",
        recipients=[email]
    )

    msg.body = f"""
Hello,

Your Lumina OTP is:

{otp}

This OTP is valid for 5 minutes.

Regards,
Lumina AI Tutor
"""

    try:
        current_app.mail.send(msg)

    except Exception as e:
        print("Email Error:", e)

        return jsonify({
            "message": f"Failed to send OTP: {str(e)}"
        }), 500

    return jsonify({
        "message": "OTP sent successfully"
    }), 200


# ================= VERIFY OTP =================
@auth_bp.route("/verify-otp", methods=["POST"])
def verify_otp():
    data = request.get_json()

    email = data.get("email")
    otp = data.get("otp")

    otp_doc = otp_collection.find_one({
        "email": email,
        "otp": otp
    })

    if not otp_doc:
        return jsonify({
            "message": "Invalid OTP"
        }), 400

    user = users.find_one({"email": email})

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    token = jwt.encode(
        {
            "email": email,
            "role": user["role"],
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(hours=24)
        },
        os.getenv("JWT_SECRET"),
        algorithm="HS256"
    )

    # Delete OTP after successful verification
    otp_collection.delete_many({
        "email": email
    })

    return jsonify({
    "message": "Login successful",
    "token": token,
    "role": user["role"],
    "fullName": user["fullName"]
}), 200
@auth_bp.route("/student/dashboard", methods=["GET"])
def student_dashboard():
    email = request.args.get("email")

    user = users.find_one({"email": email})

    if not user:
        return jsonify({"message": "User not found"}), 404

    active_courses = courses.count_documents({
        "studentEmail": email
    })

    quiz_data = list(quizzes.find({
        "studentEmail": email
    }))

    avg_score = 0

    if quiz_data:
        avg_score = round(
            sum(q["score"] for q in quiz_data) /
            len(quiz_data),
            1
        )

    study_tasks = list(tasks.find({
        "studentEmail": email,
        "status": "Completed"
    }))

    study_hours = len(study_tasks) * 2

    streak = len(study_tasks)

    return jsonify({
        "fullName": user["fullName"],
        "activeCourses": active_courses,
        "studyHours": study_hours,
        "streak": streak,
        "avgQuizScore": avg_score
    }), 200
