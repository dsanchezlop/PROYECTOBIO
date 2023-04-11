<template>
  <div id="chart"></div>
</template>

<script>
export default {
  name: "Charts",
  data() {
    return {
      countries: [],
    };
  },
  created() {
    // Get the countries from the url
    this.countries = this.$route.query.countries.split(",");
    // console.log(this.countries);
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
      console.log(data);

      });
    }
};

</script>
