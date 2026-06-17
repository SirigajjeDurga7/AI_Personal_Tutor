import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const data = [
  { day: "Mon", score: 60 },
  { day: "Tue", score: 65 },
  { day: "Wed", score: 72 },
  { day: "Thu", score: 80 },
  { day: "Fri", score: 88 },
];

function ProgressChart() {
  return (
    <div className="bg-white rounded-3xl p-6 shadow-sm">
      <h2 className="font-bold mb-4">
        Learning Progress
      </h2>

      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <XAxis dataKey="day" />
          <YAxis />
          <Tooltip />
          <Line dataKey="score" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default ProgressChart;