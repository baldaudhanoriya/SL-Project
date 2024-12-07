import React from "react";
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const Graph = ({ data }) => {
    const parsedData = React.useMemo(() => {
      const labels = [];
      const values = [];
  
      Object.entries(data).forEach(([key, value]) => {
        labels.push(key); 
        values.push(value); 
      });
  
      return { labels, values };
    }, [data]);
  
    const chartData = {
      labels: parsedData.labels,
      datasets: [
        {
          label: "Popularity Over Time",
          data: parsedData.values,
          borderColor: "rgba(75,192,192,1)",
          backgroundColor: "rgba(75,192,192,0.2)",
          borderWidth: 2,
          tension: 0.2,
          pointRadius: 3,
          pointBackgroundColor: "rgba(75,192,192,1)",
        },
      ],
    };
  
    const options = {
      responsive: true,
      plugins: {
        legend: {
          display: true,
          position: "top",
        },
        tooltip: {
          enabled: true,
        },
      },
      scales: {
        x: {
          title: {
            display: true,
            text: "Date ",
          },
        },
        y: {
          title: {
            display: true,
            text: "Popularity",
          },
        },
      },
    };
  
    return <Line data={chartData} options={options} width="400px"/>;
  };
  
export default Graph