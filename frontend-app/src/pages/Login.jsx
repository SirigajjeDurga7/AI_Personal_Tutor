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

  const [statusMessage, setStatusMessage] = useState("");
  const [statusType, setStatusType] = useState(""); 

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setStatusMessage(""); 

    try {
      // FIXED: Completely drops Render. Now dynamically points back to its own Hugging Face container domain
      const baseUrl = window.location.origin;

      const response = await axios.post(`${baseUrl}/login`, {
        email: formData.email,
        password: formData.password,
        role: role,
      });

      setStatusType("success");
      setStatusMessage(response.data.message);

      localStorage.setItem("token", response.data.token);
      localStorage.setItem(
        "currentUser",
        JSON.stringify({
          email: formData.email,
          role: response.data.role,
          fullName: response.data.fullName,
        })
      );

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
      console.error("Login Error Details:", error);
      setStatusType("error"); 

      if (!error.response) {
        setStatusMessage("Network error: Cannot reach the backend database container node.");
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

          <button type="submit">Login</button>

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
