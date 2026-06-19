import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Register from "./pages/Register";
import Login from "./pages/Login";
import VerifyOTP from "./pages/VerifyOTP";

import StudentDashboard from "./pages/StudentDashboard";


function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login/:role" element={<Login />} />
      <Route
        path="/register/:role"
        element={<Register />}
      />
      <Route
  path="/student/dashboard"
  element={<StudentDashboard />}
/>
      <Route path="/verify-otp" element={<VerifyOTP />} />
    </Routes>
  );
}

export default App;