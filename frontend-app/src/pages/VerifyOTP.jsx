import "./VerifyOTP.css";
import { useState, useEffect } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";

function VerifyOTP() {
  const location = useLocation();
  const navigate = useNavigate();

  const email = location.state?.email || "";
  const role = location.state?.role || "";

  const [otp, setOtp] = useState("");
  const [timer, setTimer] = useState(30);

  // NEW: State for tracking status feedback notifications
  const [statusMessage, setStatusMessage] = useState("");
  const [statusType, setStatusType] = useState(""); // Can be 'success' or 'error'

  useEffect(() => {
    if (timer > 0) {
      const interval = setInterval(() => {
        setTimer((prev) => prev - 1);
      }, 1000);

      return () => clearInterval(interval);
    }
  }, [timer]);

  const handleVerify = async (e) => {
    e.preventDefault();
    setStatusMessage(""); // Clear previous alerts on new submit

    try {
      // Pointing directly to your live Render backend URL
      const baseUrl = "https://ai-personal-tutor-owly.onrender.com";

      // Connects directly to the live backend domain on Render
      const response = await axios.post(`${baseUrl}/verify-otp`, {
        email,
        otp,
      });

      // Show Custom Green Success Alert Box
      setStatusType("success");
      setStatusMessage(response.data.message);

      // Save JWT Token
      localStorage.setItem("token", response.data.token);

      // Save Current User
      localStorage.setItem(
        "currentUser",
        JSON.stringify({
          email,
          role: response.data.role,
          fullName: response.data.fullName,
        })
      );

      // Wait 1.5 seconds so the user can read the nice message, then navigate
      setTimeout(() => {
        if (response.data.role === "student") {
          navigate("/student/dashboard");
        } else if (response.data.role === "instructor") {
          navigate("/instructor/dashboard");
        } else {
          navigate("/admin/dashboard");
        }
      }, 1500);

    } catch (error) {
      console.error("Verification Network Error Details:", error);
      setStatusType("error"); // Show Custom Red Error Alert Box
      
      if (!error.response) {
        setStatusMessage("Network error: Cannot reach the backend server on Render.");
      } else {
        setStatusMessage(error.response?.data?.message || "OTP Verification Failed");
      }
    }
  };

  const handleResend = () => {
    setTimer(30);
    setStatusType("error");
    setStatusMessage("Please login again to receive a new verification code.");
  };

  return (
    <div className="otp-container">
      <div className="otp-card">
        <h1>Verify OTP</h1>
        <p>Enter the OTP sent to</p>
        <span className="user-email-display">{email}</span>

        <form onSubmit={handleVerify}>
          <input
            type="text"
            maxLength="6"
            placeholder="Enter 6-digit OTP"
            value={otp}
            onChange={(e) => setOtp(e.target.value)}
            required
          />
          <button type="submit">Verify OTP</button>

          {/* NEW: Dynamic Embedded Status Notification Boxes */}
          {statusMessage && (
            <div className={`status-box ${statusType}-box`}>
              {statusMessage}
            </div>
          )}
        </form>

        {timer > 0 ? (
          <p className="timer">Resend OTP in {timer}s</p>
        ) : (
          <button className="resend-btn" onClick={handleResend}>
            Resend OTP
          </button>
        )}
      </div>
    </div>
  );
}

export default VerifyOTP;
