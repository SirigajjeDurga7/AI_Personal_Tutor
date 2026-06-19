// src/pages/StudentDashboard.jsx

import "./StudentDashboard.css";
import { useEffect, useState } from "react";
import axios from "axios";
function StudentDashboard() {
  const currentUser = JSON.parse(
  localStorage.getItem("currentUser")
);

const [dashboardData, setDashboardData] = useState(null);

useEffect(() => {
  fetchDashboard();
}, []);

const fetchDashboard = async () => {
  try {
    const response = await axios.get(
      "http://localhost:5000/student/dashboard",
      {
        params: {
          email: currentUser.email,
        },
      }
    );

    setDashboardData(response.data);

  } catch (error) {
    console.error(error);
  }
};

  const stats = [
  {
    title: "ACTIVE COURSES",
    value: dashboardData.stats.activeCourses,
    subtitle: "Enrolled",
    icon: "📚",
  },
  {
    title: "STUDY HOURS",
    value: dashboardData.stats.studyHours,
    subtitle: "Completed",
    icon: "🕒",
  },
  {
    title: "CURRENT STREAK",
    value: dashboardData.stats.streak,
    subtitle: "days",
    icon: "🔥",
  },
  {
    title: "AVG. QUIZ SCORE",
    value: `${dashboardData.stats.avgQuizScore}%`,
    subtitle: "Average",
    icon: "🏆",
  },
];

  const courses = dashboardData.courses;
   

  const quizzes = dashboardData.quizzes;
  if (!dashboardData) {
  return <h2>Loading Dashboard...</h2>;
}
  return (
    <div className="dashboard-layout">

      {/* Sidebar */}
      <aside className="sidebar">

        <div className="logo">
          <div className="logo-icon">🎓</div>

          <div>
            <h2>Lumina</h2>
            <p>AI LMS</p>
          </div>
        </div>

        <div className="menu-section">

          <span>Learn</span>

          <ul>

            <li className="active">Dashboard</li>

            <li>Courses</li>

            <li>Notes</li>

          </ul>

        </div>

        <div className="menu-section">

          <span>AI Tools</span>

          <ul>

            <li>AI Tutor</li>

            <li>Quizzes</li>

            <li>Flashcards</li>

            <li>Study Planner</li>

          </ul>

        </div>

        <div className="menu-section">

          <span>Insights</span>

          <ul>

            <li>Progress</li>

          </ul>

        </div>

        <div className="profile-box">

          <div className="avatar">
            {dashboardData.fullName.charAt(0)}
          </div>

          <div>

            <h4>{dashboardData.fullName}</h4>

            <p>Student</p>

          </div>

        </div>

      </aside>

      {/* Main */}

      <main className="dashboard-content">

        {/* Topbar */}

        <header className="topbar">

          <input
            className="search"
            placeholder="Search courses, notes, students..."
          />

          <div className="topbar-right">

            <button className="ai-active">
              ✨ AI Active
            </button>

            <button className="notification">
              🔔
            </button>

            <div className="top-avatar">
              {currentUser.fullName.charAt(0)}
            </div>

          </div>

        </header>

        {/* Welcome */}

        <div className="welcome-section">

          <div>

            <h1>
              Welcome back, {dashboardData.fullName} 👋 👋
            </h1>

            <p>
              Here's a snapshot of your learning today.
            </p>

          </div>

          <button className="tutor-btn">
            🤖 Ask AI Tutor
          </button>

        </div>

        {/* Stats */}

        <div className="stats-grid">

          {stats.map((stat, index) => (

            <div
              key={index}
              className="stat-card"
            >

              <div className="stat-top">

                <span>{stat.title}</span>

                <div className="stat-icon">
                  {stat.icon}
                </div>

              </div>

              <h2>{stat.value}</h2>

              <p>{stat.subtitle}</p>

            </div>

          ))}

        </div>

        {/* Learning + Study */}

        <div className="middle-grid">

          <div className="learning-card">

            <div className="card-header">

              <h3>Continue learning</h3>

              <button>View all →</button>

            </div>

            {courses.map((course, index) => (

              <div
                className="course-item"
                key={index}
              >

                <div
                  className="course-icon"
                  style={{
                    background: course.color,
                  }}
                />

                <div className="course-info">

                  <div className="course-title-row">

                    <h4>{course.courseName}</h4>

                    <span>
                      {course.level}
                    </span>

                  </div>

                  <p>
                    {course.instructor}
                    {" • "}
                    {course.duration}
                  </p>

                  <div className="progress-row">

                    <div className="progress-bar">

                      <div
                        className="progress-fill"
                        style={{
                          width:
                            `${course.progress || 0}%`,
                        }}
                      />

                    </div>

                    <span>
                      {course.progress || 0}%
                    </span>

                  </div>

                </div>

              </div>

            ))}

          </div>

          <div className="study-card">

            <h3>Weekly study hours</h3>

            <div className="study-chart">

              <div className="days">

                <span>Mon</span>
                <span>Tue</span>
                <span>Wed</span>
                <span>Thu</span>
                <span>Fri</span>
                <span>Sat</span>
                <span>Sun</span>

              </div>

              <p>
                Total:
                <strong>
                  {" "}22.3 hrs
                </strong>
                {" "}this week
              </p>

            </div>

          </div>

        </div>

        {/* Bottom */}

        <div className="bottom-grid">

          <div className="quiz-card">

            <div className="card-header">

              <h3>Recent quizzes</h3>

              <button>
                All quizzes
              </button>

            </div>

            {quizzes.map((quiz, index) => (

              <div
                className="quiz-item"
                key={index}
              >

                <div>

                  <h4>{quiz.title}</h4>

                  <p>{quiz.subject}</p>

                </div>

                <span className="score">

                  {quiz.score}%

                </span>

              </div>

            ))}

          </div>

          <div className="tip-card">

            <h3>
              ✨ AI Tip of the day
            </h3>

            <p>
              "Active recall beats
              re-reading. Try a
              5-card flashcard sprint
              after each chapter."
            </p>

            <button>
              Start flashcard sprint
            </button>

          </div>

        </div>

      </main>

    </div>
  );
}

export default StudentDashboard;