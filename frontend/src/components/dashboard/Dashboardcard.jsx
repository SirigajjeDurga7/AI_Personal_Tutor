function DashboardCard({ title, value, icon }) {
  return (
    <div className="bg-white rounded-3xl shadow-sm p-6 hover:shadow-lg transition">
      <div className="text-blue-600 text-3xl">
        {icon}
      </div>

      <h3 className="mt-4 text-gray-500">
        {title}
      </h3>

      <h1 className="text-3xl font-bold">
        {value}
      </h1>
    </div>
  );
}

export default DashboardCard;