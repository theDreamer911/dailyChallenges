let myChart = document.getElementById("myChart").getContext("2d");

// Global Options
Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = "#777";

let massPopChart = new Chart(myChart, {
  type: "radar", // Bar, horizontalBar, pie, line, doughnut, radar, plarArea, and others, doughnut
  data: {
    labels: ["Boston", "Worcester", "Springfield", "Cambridge", "Lowell"],
    datasets: [
      {
        label: "Population",
        data: [695506, 185174, 152160, 120479, 110267],
        // backgroundColor: "green",
        backgroundColor: ["red", "green", "blue", "yellow", "orange"],
        borderWidth: 4,
        borderColor: "#000",
        hoverBorderWidth: 3,
        hoverBorderColor: "#fff",
      },
    ],
  },
  options: {
    title: {
      display: true,
      text: "Largest Cities In Massachusetts",
      fontSize: 25,
    },
    legend: {
      display: true,
      position: "right",
      labels: {
        fontColor: "#000",
      },
    },
    layout: {
      padding: {
        left: 50,
        right: 0,
        bottom: 0,
        top: 0,
      },
    },
    tooltips: {
      enabled: true,
    },
  },
});
