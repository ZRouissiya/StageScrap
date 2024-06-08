const getMainChartOptions = (secteurs, seriesData) => {
  let mainChartColors = {};
  if (document.documentElement.classList.contains("dark")) {
    mainChartColors = {
      borderColor: "#374151",
      labelColor: "#9CA3AF",
      opacityFrom: 0,
      opacityTo: 0.15,
    };
  } else {
    mainChartColors = {
      borderColor: "#F3F4F6",
      labelColor: "#6B7280",
      opacityFrom: 0.45,
      opacityTo: 0,
    };
  }
  return {
    chart: {
      height: 420,
      type: "area",
      fontFamily: "Inter, sans-serif",
      foreColor: mainChartColors.labelColor,
      toolbar: { show: false },
    },
    fill: {
      type: "gradient",
      gradient: {
        enabled: true,
        opacityFrom: mainChartColors.opacityFrom,
        opacityTo: mainChartColors.opacityTo,
      },
    },
    dataLabels: { enabled: false },
    tooltip: { style: { fontSize: "14px", fontFamily: "Inter, sans-serif" } },
    grid: {
      show: true,
      borderColor: mainChartColors.borderColor,
      strokeDashArray: 1,
      padding: { left: 35, bottom: 15 },
    },
    series: seriesData,
    markers: {
      size: 5,
      strokeColors: "#ffffff",
      hover: { size: undefined, sizeOffset: 3 },
    },
    xaxis: {
      categories: secteurs,
      labels: {
        style: {
          colors: [mainChartColors.labelColor],
          fontSize: "14px",
          fontWeight: 500,
        },
      },
      axisBorder: { color: mainChartColors.borderColor },
      axisTicks: { color: mainChartColors.borderColor },
      crosshairs: {
        show: true,
        position: "back",
        stroke: { color: mainChartColors.borderColor, width: 1, dashArray: 10 },
      },
    },
    yaxis: {
      labels: {
        style: {
          colors: [mainChartColors.labelColor],
          fontSize: "14px",
          fontWeight: 500,
        },
        formatter: function (value) {
          return value;
        },
      },
    },
    legend: {
      fontSize: "14px",
      fontWeight: 500,
      fontFamily: "Inter, sans-serif",
      labels: { colors: [mainChartColors.labelColor] },
      itemMargin: { horizontal: 10 },
    },
    responsive: [
      { breakpoint: 1024, options: { xaxis: { labels: { show: false } } } },
    ],
  };
};
if (document.getElementById("main-chart")) {
  fetch("/graph-data-secteurs")
    .then((response) => response.json())
    .then((data) => {
      const categories = data.dates;
      const secteurs = new Set();
      const seriesData = {};
      categories.forEach((date) => {
        for (const secteur in data.data[date]) {
          secteurs.add(secteur);
        }
      });
      secteurs.forEach((secteur) => {
        seriesData[secteur] = categories.map(
          (date) => data.data[date][secteur] || 0
        );
      });
      const series = Array.from(secteurs).map((secteur) => ({
        name: secteur,
        data: seriesData[secteur],
      }));
      const chart = new ApexCharts()(
        document.getElementById("main-chart"),
        getMainChartOptions(categories, series)
      );
      chart.render();
      document.addEventListener("dark-mode", function () {
        chart.updateOptions(getMainChartOptions(categories, series));
      });
    })
    .catch((error) => console.error("Error fetching chart data:", error));
}
if (document.getElementById("niveau-chart")) {
  fetch("/graph-data-niveau")
    .then((response) => response.json())
    .then((data) => {
      const options = {
        colors: ["#1A56DB"],
        series: [
          {
            name: "Postes",
            color: "#1A56DB",
            data: data.map((item) => ({ x: item.level, y: item.count })),
          },
        ],
        chart: {
          type: "bar",
          height: "140px",
          fontFamily: "Inter, sans-serif",
          foreColor: "#4B5563",
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            columnWidth: "90%",
            borderRadius: 3,
          },
        },
        tooltip: {
          shared: false,
          intersect: false,
          style: { fontSize: "14px", fontFamily: "Inter, sans-serif" },
        },
        states: { hover: { filter: { type: "darken", value: 1 } } },
        stroke: { show: true, width: 5, colors: ["transparent"] },
        grid: { show: false },
        dataLabels: { enabled: false },
        legend: { show: false },
        xaxis: {
          floating: false,
          labels: { show: false },
          axisBorder: { show: false },
          axisTicks: { show: false },
        },
        yaxis: { show: false },
        fill: { opacity: 1 },
      };
      const chart = new ApexCharts()(
        document.getElementById("niveau-chart"),
        options
      );
      chart.render();
    })
    .catch((error) => console.error("Error fetching chart data:", error));
}
const getDomaineChartOptions = (data) => {
  let domaineChartColors = {};
  if (document.documentElement.classList.contains("dark")) {
    domaineChartColors = {
      backgroundBarColors: [
        "#374151",
        "#374151",
        "#374151",
        "#374151",
        "#374151",
        "#374151",
        "#374151",
      ],
    };
  } else {
    domaineChartColors = {
      backgroundBarColors: [
        "#E5E7EB",
        "#E5E7EB",
        "#E5E7EB",
        "#E5E7EB",
        "#E5E7EB",
        "#E5E7EB",
        "#E5E7EB",
      ],
    };
  }
  return {
    series: [{ name: "Postes", data: data.counts }],
    labels: data.domaines,
    chart: {
      type: "bar",
      height: "140px",
      foreColor: "#4B5563",
      fontFamily: "Inter, sans-serif",
      toolbar: { show: false },
    },
    theme: { monochrome: { enabled: true, color: "#1A56DB" } },
    plotOptions: {
      bar: {
        columnWidth: "25%",
        borderRadius: 3,
        colors: {
          backgroundBarColors: domaineChartColors.backgroundBarColors,
          backgroundBarRadius: 3,
        },
      },
      dataLabels: { hideOverflowingLabels: false },
    },
    xaxis: {
      floating: false,
      labels: { show: false },
      axisBorder: { show: false },
      axisTicks: { show: false },
    },
    tooltip: {
      shared: true,
      intersect: false,
      style: { fontSize: "14px", fontFamily: "Inter, sans-serif" },
    },
    states: { hover: { filter: { type: "darken", value: 0.8 } } },
    fill: { opacity: 1 },
    yaxis: { show: false },
    grid: { show: false },
    dataLabels: { enabled: false },
    legend: { show: false },
  };
};
if (document.getElementById("domaine-chart")) {
  fetch("/graph-data-domaine")
    .then((response) => response.json())
    .then((data) => {
      const chart = new ApexCharts()(
        document.getElementById("domaine-chart"),
        getDomaineChartOptions(data)
      );
      chart.render();
      document.addEventListener("dark-mode", function () {
        chart.updateOptions(getDomaineChartOptions(data));
      });
    })
    .catch((error) => console.error("Error fetching chart data:", error));
}
