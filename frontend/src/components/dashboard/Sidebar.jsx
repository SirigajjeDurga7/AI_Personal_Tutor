import "./dashboard.css";

function Sidebar({ role }) {
  return (
    <div className="sidebar">
      <h2>AI Tutor</h2>

      <ul>
        <li>Dashboard</li>
        <li>Courses</li>
        <li>AI Tutor</li>

        {role === "Student" && <li>Progress</li>}
        {role === "Instructor" && <li>Students</li>}
        {role === "Admin" && <li>Analytics</li>}
      </ul>
    </div>
  );
}

export default Sidebar;