import DashboardCard from "../../components/dashboard/DashboardCard";
import ProgressChart from "../../components/dashboard/ProgressChart";

import {
  BookOpen,
  Brain,
  Trophy,
  Flame
} from "lucide-react";

function Dashboard() {
  return (
    <div className="p-8 bg-slate-50 min-h-screen">

      <h1 className="text-4xl font-bold mb-2">
        Welcome Back Khushi 👋
      </h1>

      <p className="text-gray-500 mb-8">
        Here's your learning overview
      </p>

      <div className="grid md:grid-cols-4 gap-6">

        <DashboardCard
          title="Courses"
          value="8"
          icon={<BookOpen />}
        />

        <DashboardCard
          title="Quiz Avg"
          value="84%"
          icon={<Trophy />}
        />

        <DashboardCard
          title="AI Tutor Chats"
          value="21"
          icon={<Brain />}
        />

        <DashboardCard
          title="Study Streak"
          value="12 Days"
          icon={<Flame />}
        />

      </div>

      <div className="mt-8">
        <ProgressChart />
      </div>

    </div>
  );
}

export default Dashboard;