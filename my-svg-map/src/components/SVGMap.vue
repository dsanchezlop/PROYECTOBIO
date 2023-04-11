<template>
  <div
    class="prio2"
    style="display: flex; justify-content: center; margin-top: 10px"
  >
    <h3>Select year</h3>
    <input
      type="range"
      min="1961"
      max="2019"
      step="1"
      id="year-slider"
      v-model="selectedYear"
      @change="updateMap"
    />
    <span>{{ selectedYear }}</span>
    <button id="play-button">Play</button>
  </div>
  <h3>Select fertilizer</h3>
  <select class="prio" @change="updateFertilizerType">
    <option value="nitrogen">Nitrogen Derived</option>
    <option value="phosphorous">Phosphorous Derived</option>
    <option value="potassium">Potassium Derived</option>
  </select>
  <br />
  <br />
  <button class="button-zoom" @click="zoomIn">+</button>
  <button class="button-zoom" @click="zoomOut">-</button>
  <br />
  <br />
  <button class="button-container" @click="clearSelection">
    Clear Selection
  </button>
  <br />
  <button
    v-if="selectedStates.length > 1"
    class="button-container"
    @click="navigateToCharts"
  >
    Go to charts
  </button>

  <div class="prio">
    <div style="display: flex; text-align: center; align-items: center">
      <h3>Hovered Country:</h3>
      <h3 style="color: red" id="hover-value2">Move your mouse</h3>
    </div>
    <h2>Selected Countries:</h2>
    <div style="display: inline">
      <!-- up to down -->
      <h4 v-for="state in selectedStates" :key="state.id">
        {{ state.id }}: {{ state.title }}
      </h4>

      <!-- right to left -->
      <!-- <h4 style="display:inline; margin:10px;" v-for="state in selectedStates" :key="state.id"> {{ state.id }} :
           {{ state.title }} </h4> -->
    </div>
  </div>

  <div
    ref="chart"
    style="
      position: relative;
      width: 75%;
      height: 80%;
      margin-left: 25%;
      margin-top: 33%;
    "
  ></div>
</template>

<script>
import { ref, reactive } from "vue";
import * as d3 from "d3";
import axios from "axios";

const selectedFertilizer = ref("nitrogen");

export default {
  data() {
    return {
      selectedStates: ref([]),
      currentZoom: 1,
      name: "charts",
      selectedYear: 1961,
    };
  },
  mounted() {
    const svg = d3
      .select(this.$refs.chart)
      .append("svg")
      .attr("width", "75%")
      .attr("height", "100%")
      .style("position", "fixed")
      .style("left", "25%")
      .style("top", "20%");

    // World svg loading and drawn
    d3.xml(require("@/assets/world.svg"))
      .then((data) => {
        //Calls to the function after loading and drawing the svg map
        this.getDataFromAPI();

        const importedNode = document.importNode(data.documentElement, true);
        svg.node().appendChild(importedNode);

        //Gets all SVG "path" elements
        const paths = svg.selectAll("path");

        // Assing the functions "changeColorOnClick", "changeColorOnHover" y "restoreColorOnHover" to the corresponding events of each "path" element
        paths
          .on("click", this.changeColorOnClick)
          .on("mouseover", this.changeColorOnHover)
          .on("mouseout", this.restoreColorOnHover);

        // Adds zoom to the map
        const zoom = d3
          .zoom()
          .scaleExtent([1, 8]) // Defined zoom limits
          .on("zoom", this.zoomed); // Calls to the zoom function each time it's used

        svg.call(zoom); // Calls to the zoom function in the SVG element

        // Initialize zoom
        this.currentZoom = 1;
      })
      .catch((error) => {
        console.error(error);
      });
    const countries = this.$route.query.countries;
    if (countries) {
      const countryList = countries.split(",");
      const selectedCountries = countryList.join(", ");
    }

    //Add the event controller to the slider controller
    const yearSlider = document.getElementById("year-slider");
    yearSlider.addEventListener("input", (event) => {
      this.updateMap(event.target.value);
    });
  },
  methods: {
    //Function to change the background color of a "path" element Función para cambiar el color de fondo de un elemento "path" a verde al hacer clic en él
    changeColorOnClick(event) {
      const path = event.target;

      if (path.classList.contains("selectedPath")) {
        // If selected, the color resets
        // path.style.fill = 'black';
        this.updateMapColors();
        path.classList.remove("selectedPath");
        // Removes the country from the selected list
        this.selectedStates = this.selectedStates.filter(
          (state) => state.id !== path.id
        );
      } else {
        // If not selected, changes color
        path.style.fill = "green";
        path.classList.add("selectedPath");
        // Adds country to the selected country list
        this.selectedStates.push({
          id: path.id,
          title: path.getAttribute("title"),
        });
        console.log(this.selectedStates);
      }
    },

    // Function to change the background color of a "path" element to blue on hover
    changeColorOnHover(event) {
      const path = event.target;
      if (!path.classList.contains("selectedPath")) {
        path.style.fill = "blue";
        document.getElementById("hover-value2").textContent =
          path.getAttribute("title");
      } else {
        path.style.fill = "green";
      }
    },

    // Function to restore the background color of a "path" element when you stop hovering the mouse over it
    restoreColorOnHover(event) {
      const path = event.target;

      if (!path.classList.contains("selectedPath")) {
        // path.style.fill = 'black';
        this.updateMapColors();
      }
    },
    // Function to empty the array and remove the color of the selected countries
    clearSelection() {
      // Empty the array of selected countries
      this.selectedStates.splice(0);

      // Deselect all DOM elements that have class "selectedPath"
      const selectedPaths = document.querySelectorAll(".selectedPath");
      selectedPaths.forEach((element) => {
        element.classList.remove("selectedPath");
        // element.style.fill = "black";
        this.updateMapColors();
      });
    },

    // Zoom function used by the button
    zoomIn() {
      this.currentZoom = Math.min(this.currentZoom / 0.9, 1.5); // Increase the current zoom factor and make sure it doesn't exceed the maximum limit
      d3.select("svg") // Select the SVG element
        .transition() // Add animated transition to zoom
        .duration(500) // Duration of the transition (in miliseconds)
        .attr("transform", "scale(" + this.currentZoom + ")"); // Apply zoom transform
    },
    // Zoom function used by the button
    zoomOut() {
      this.currentZoom = Math.max(this.currentZoom * 0.9, 0.5); // Decrease the current zoom factor and make sure it doesn't exceed the maximum limit
      d3.select("svg") // Select the SVG element
        .transition() // Add animated transition to zoom
        .duration(500) // Duration of the transition (in miliseconds)
        .attr("transform", "scale(" + this.currentZoom + ")"); // Apply zoom transform
    },
    // Function to zoom with the mouse scroll and drag the map
    zoomed(event) {
      this.currentZoom = event.transform.k;
      d3.select("svg").attr("transform", event.transform); // Aplicar la transformación al elemento SVG actual
    },
    navigateToCharts() {
      const selectedCountries = this.selectedStates
        .map((state) => state.title)
        .join(",");
      this.$router.push({
        name: "charts",
        query: { countries: selectedCountries },
      });
    },
    getDataFromAPI() {
      const apiUrl = `http://49.12.36.190/api/fertilizers-${selectedFertilizer.value}-year?year=${this.selectedYear}`;

      axios
        .get(apiUrl)
        .then((response) => {
          const data = response.data;
          this.updateMapValues(data);
        })
        .catch((error) => {
          console.error(error);
        });
    },

    updateMapValues(data) {
      const paths = document.querySelectorAll("path");
      const tooltip = document.createElement("div"); // Creates the div element for the tooltip
      tooltip.style.position = "absolute";
      tooltip.style.backgroundColor = "white";
      tooltip.style.border = "1px solid gray";
      tooltip.style.padding = "5px";
      tooltip.style.pointerEvents = "none";
      tooltip.style.display = "none"; // Hides the tooltip by default
      document.body.appendChild(tooltip); // Adds the tooltip to the body

      paths.forEach((path) => {
        const code = path.getAttribute("id");
        const value = data.find((item) => item.code === code)?.amount ?? 0;
        path.setAttribute("amount", value);

        path.addEventListener("mouseover", () => {
          // Gets the mouse position and updates the tooltip
          const x = event.clientX;
          const y = event.clientY;
          tooltip.style.top = `${y}px`;
          tooltip.style.left = `${x}px`;
          tooltip.style.display = "block"; // Shows the tooltip
          tooltip.textContent = `${path.getAttribute("title")}: ${value}`;
        });

        path.addEventListener("mousemove", () => {
          // Updates the tooltip while the mouse moves inside the "path"
          const x = event.clientX;
          const y = event.clientY;
          tooltip.style.top = `${y}px`;
          tooltip.style.left = `${x}px`;
        });

        path.addEventListener("mouseout", () => {
          // Hide the tooltip when the mouse leaves the "path" element
          tooltip.style.display = "none";
        });
      });
      this.updateMapColors();
    },
    createLegend(colorScale, colors) {
      // Delete the previous legend if it exists
      const existingLegend = document.getElementById("legend-container");
      if (existingLegend) {
        existingLegend.remove();
      }

      const legendContainer = document.createElement("div");
      legendContainer.setAttribute("id", "legend-container");
      legendContainer.style.display = "flex";
      legendContainer.style.flexDirection = "row";
      legendContainer.style.alignItems = "center";
      legendContainer.style.justifyContent = "center";
      legendContainer.style.marginTop = "10px";

      colors.forEach((color, index) => {
        const colorBox = document.createElement("div");
        colorBox.style.backgroundColor = color;
        colorBox.style.width = "20px";
        colorBox.style.height = "20px";
        colorBox.style.margin = "0 5px";

        const rangeText = document.createElement("span");
        rangeText.style.marginLeft = "5px";
        rangeText.style.marginRight = "10px";
        const range = colorScale.invertExtent(color);
        // Special case for the first range (0.00 - 0.00)
        if (index === 0) {
          rangeText.textContent = `${range[0].toFixed(2)} - ${range[0].toFixed(
            2
          )}`;
        } else {
          rangeText.textContent = `${range[0].toFixed(2)} - ${range[1].toFixed(
            2
          )}`;
        }

        const legendItem = document.createElement("div");
        legendItem.style.display = "flex";
        legendItem.style.alignItems = "center";
        legendItem.appendChild(colorBox);
        legendItem.appendChild(rangeText);

        legendContainer.appendChild(legendItem);
      });

      // Adds legend at the end of the body
      document.body.appendChild(legendContainer);
    },
    updateMapColors() {
      const paths = document.querySelectorAll("path");
      const colors = [
        "#F5E1F7",
        "#E6B8E6",
        "#D7A3D3",
        "#C68FC6",
        "#B67AB6",
        "#A666A3",
        "#965291",
        "#854D80",
        "#73386E",
        "#62245C",
      ];
      const amounts = Array.from(paths, (path) =>
        Number(path.getAttribute("amount"))
      );
      const maxAmount = Math.max(...amounts);
      const colorScale = d3
        .scaleQuantile()
        .domain(amounts.filter((amount) => amount > 0)) // Excludes the value 0.00 from the scale
        .range(colors.slice(1)); // Excludes the first color in the range, as it will be handled separately

      paths.forEach((path) => {
        const amount = Number(path.getAttribute("amount"));
        const color = amount === 0 ? colors[0] : colorScale(amount); // Use the first color of the array for the range 0.00 - 0.00
        path.style.fill = color;
      });

      // Creates the legend
      this.createLegend(colorScale, colors);
    },

    updateFertilizerType(event) {
      selectedFertilizer.value = event.target.value;
      this.getDataFromAPI();
    },

    addLegend() {
      // Delete the previous legend if it exists
      const existingLegend = document.getElementById("map-legend");
      if (existingLegend) {
        existingLegend.remove();
      }

      // Below is the existing code to add the legend
      const legend = L.control({ position: "bottomright" });

      legend.onAdd = () => {
        const div = L.DomUtil.create("div", "info legend");
        div.id = "map-legend"; // Add an ID so we can easily select and remove it
        const grades = this.legendGrades;
        const labels = [];

        for (let i = 0; i < grades.length; i++) {
          labels.push(
            '<i style="background:' +
              this.getColor(grades[i] + 1) +
              '"></i> ' +
              grades[i] +
              (grades[i + 1] ? "&ndash;" + grades[i + 1] + "<br>" : "+")
          );
        }

        div.innerHTML = labels.join("");
        return div;
      };

      legend.addTo(this.map);
    },
    updateMap(year) {
      // Aquí es donde puedes actualizar el mapa con los datos correspondientes al año
      console.log("Año seleccionado:", year);
      // Llama a las funciones necesarias para actualizar el mapa aquí
    },
    playYears() {
      const startYear = 1961;
      const endYear = 2019;
      let currentYear = startYear;

      const interval = setInterval(() => {
        updateMap(currentYear);
        yearSlider.value = currentYear;
        currentYear++;

        if (currentYear > endYear) {
          clearInterval(interval);
        }
      }, 1000); // Change every 1000 milliseconds (1 second)
    },
    updateMap() {
      this.getDataFromAPI();
    },
  },
};
</script>

<style scoped>
button {
  background-color: #604caf;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background-color: #3b285f;
}

.prio {
  position: relative;
  z-index: 1;
  margin-right: auto;
  width: fit-content;
  height: fit-content;
}

.prio2 {
  position: relative;
  z-index: 1;
}

h2,
h3,
h4 {
  color: red;
}

.selectedPath {
  animation-name: slowchange;
  animation-duration: 1.5s;
  animation-fill-mode: forwards;
  transition: fill 0.5s ease-in-out;
}

path:hover {
  animation-name: hoverChange;
  animation-duration: 1s;
  animation-fill-mode: forwards;
}

.map-container {
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}

.button-container {
  position: relative;
  z-index: 1;
  margin-right: auto;
  width: fit-content;
  height: fit-content;
}

.button-zoom {
  position: relative;
  z-index: 1;
  margin: auto;
  width: 2%;
  height: 2%;
}

.draggeable {
  cursor: move;
}

.selected {
  fill: green;
}

path:hover {
  animation-name: hoverChange;
  animation-duration: 1s;
  animation-fill-mode: forwards;
  transition: fill 0.5s ease-in-out;
}

#legend-container {
  position: absolute;
  bottom: -50px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
}

#year-slider {
  width: 50%;
}

/* div[ref="chart"] {
  margin-bottom: 50px;
} */
</style>
