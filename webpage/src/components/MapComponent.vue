<template>
    <div id="chartdiv"></div>
</template>

  
<script>
import * as am5maps from "@amcharts/amcharts5/maps";
import * as am5geodata_worldLow from "@amcharts/amcharts5-geodata/worldLow";

export default {
  name: "MapComponent",
  mounted() {
    const chart = am5maps.MapChart.new("chartdiv");
    chart.geoData = am5geodata_worldLow;

    const polygonSeries = chart.series.push(
      new am5maps.MapPolygonSeries()
    );

    const polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.tooltipText = "{name}";
    polygonTemplate.fillOpacity = 0.8;

    polygonSeries.data = [
      {
        id: "US",
        name: "United States",
        value: 100,
        mapPolygon: chart.geoData.features.find(({ id }) => id === "US"),
      },
    ];

    chart.zoomControl = new am5maps.ZoomControl();
    chart.zoomControl.slider.height = "80%";
    chart.zoomControl.slider.step = 0.1;
  },
};
</script>

  
<style scoped>
/* Component styles go here */
</style>
