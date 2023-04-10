<template>
  <div id="chart"></div>
</template>

<script>
import * as d3 from "d3";

export default {
  data() {
    return {
      data: [
        { date: "2022-01-01", value: 100 },
        { date: "2022-02-01", value: 150 },
        { date: "2022-03-01", value: 200 },
        { date: "2022-04-01", value: 250 },
        { date: "2022-05-01", value: 300 },
        { date: "2022-06-01", value: 350 },
      ],
      lines: [],
    };
  },

  mounted() {
    this.createChart();
  },

  methods: {
    createChart() {
      const svg = d3
        .select("#chart")
        .append("svg")
        .attr("width", 600)
        .attr("height", 400);

      const margin = { top: 20, right: 20, bottom: 30, left: 50 };
      const width = +svg.attr("width") - margin.left - margin.right;
      const height = +svg.attr("height") - margin.top - margin.bottom;
      const g = svg
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      const xScale = d3
        .scaleTime()
        .domain(d3.extent(this.data, (d) => new Date(d.date)))
        .range([0, width]);

      const yScale = d3
        .scaleLinear()
        .domain([0, d3.max(this.data, (d) => d.value)])
        .range([height, 0]);

      const line = d3
        .line()
        .x((d) => xScale(new Date(d.date)))
        .y((d) => yScale(d.value));

      g.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(xScale).tickFormat(d3.timeFormat("%Y-%m-%d")));

      g.append("g").call(d3.axisLeft(yScale));

      g.append("path")
        .datum(this.data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 2)
        .attr("d", line);
    },
  },
};
</script>
