import "./Login.css";
import { useState } from "react";
import axios from "axios";
import { useParams, Link, useNavigate } from "react-router-dom";

function Login() {
  const { role } = useParams();
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  // State for tracking status feedback notifications
  const [statusMessage, setStatusMessage] = useState("");
  const [statusType, setStatusType] = useState(""); // Can be 'success' or 'error'

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setStatusMessage(""); // Clear previous alerts on new submit

    try {
      // FIXED: Pointing directly to your active live Render backend server URL endpoint
      const baseUrl = "https://onrender.com";

      const response = await axios.post(`${baseUrl}/login`, {
        email: formData.email,
        password: formData.password,
        role: role,
      });

      // Show Custom Green Success Alert Box
      setStatusType("success");
      setStatusMessage(response.data.message);

      // FIXED: Save JWT Session Token right into local storage memory
      localStorage.setItem("token", response.data.token);

      // FIXED: Save current session user data configuration objects
      localStorage.setItem(
        "currentUser",
        JSON.stringify({
          email: formData.email,
          role: response.data.role,
          fullName: response.data.fullName,
        })
      );

      // FIXED: Bypasses OTP screen steps entirely; directly navigates based on role match
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
      console.error("Login Network Error Details:", error);
      setStatusType("error"); // Show Custom Red Error Alert Box

      if (!error.response) {
        setStatusMessage("Network error: Cannot reach the backend server on Render.");
      } else {
        setStatusMessage(error.response?.data?.message || "Login failed");
      }
    }
  };

  return (
    <div className="login-container">
      <div className="login-card">
        <h1>{role.charAt(0).toUpperCase() + role.slice(1)} Login</h1>
        <p>Welcome back! Sign in to continue.</p>

        <form onSubmit={handleLogin}>
          <input
            type="text"
            name="email"
            placeholder="Email Address"
            required
            value={formData.email}
            onChange={handleChange}
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            required
            value={formData.password}
            onChange={handleChange}
          />

          {/* FIXED: Button text renamed from 'Send OTP' to standard 'Login' */}
          <button type="submit">Login</button>

          {/* Dynamic Embedded In-Card Notification Boxes */}
          {statusMessage && (
            <div className={`status-box ${statusType}-box`}>
              {statusMessage}
            </div>
          )}
        </form>

        <p className="register-link">
          Don't have an account?{" "}
          <Link to={`/register/${role}`}>Register</Link>
        </p>
      </div>
    </div>
  );
}

export default Login;
