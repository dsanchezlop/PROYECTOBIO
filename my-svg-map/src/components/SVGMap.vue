<template>
   <button class="button-zoom" @click="zoomIn">+</button>
   <button class="button-zoom" @click="zoomOut">-</button>
   <br>
   <button class="button-container" @click="clearSelection"> Clear Selection </button>
   <br>
   <button v-if="selectedStates.length > 1" class="button-container" @click="navigateToCharts">Go to charts</button>

   <div class="prio">
      <div style="display:flex; text-align: center; align-items: center;">
         <h2>Hovered Country:</h2>
         <h3 style="color: red" id="hover-value2">Move your mouse</h3>
      </div>
      <h2>Selected Countries:</h2>
      <div style="display:inline">
         <!-- up to down -->
         <h4 v-for="state in selectedStates" :key="state.id">
            {{ state.id }}: {{ state.title }}
         </h4>

         <!-- right to left -->
         <!-- <h4 style="display:inline; margin:10px;" v-for="state in selectedStates" :key="state.id"> {{ state.id }} :
           {{ state.title }} </h4> -->
      </div>

   </div>
   <select @change="updateFertilizerType">
      <option value="nitrogen">Nitrogen Derived</option>
      <option value="phosphorous">Phosphorous Derived</option>
      <option value="potassium">Potassium Derived</option>
   </select>
   <div ref="chart" style="position: relative; width: 75%; height: 80%; margin-left: 25%; margin-top: 33%;">
   </div>
   <div style="display: flex; justify-content: center; margin-top: 10px;">
      <input type="range" id="year-slider" min="1961" max="2019" step="1" value="1961">
      <button id="play-button">Play</button>
   </div>
</template>


<script>
import { ref, reactive } from 'vue';
import * as d3 from "d3";
import axios from 'axios';

const selectedFertilizer = ref('nitrogen');

export default {
   data() {
      return {
         selectedStates: ref([]),
         currentZoom: 1,
         name: "charts"
      }
   },
   mounted() {
      const svg = d3.select(this.$refs.chart)
         .append("svg")
         .attr('width', '75%')
         .attr('height', '100%')
         .style("position", "fixed")
         .style('left', '25%')
         .style('top', '20%');

      // Aquí es donde se carga el archivo world.svg y se agrega al SVG
      d3.xml(require("@/assets/world.svg"))
         .then(data => {

            // Llama a la función después de cargar y agregar el mapa SVG
            this.getDataFromAPI();

            const importedNode = document.importNode(data.documentElement, true);
            svg.node().appendChild(importedNode);

            // Obtener todos los elementos "path" del SVG
            const paths = svg.selectAll('path');

            // Asignar las funciones "changeColorOnClick", "changeColorOnHover" y "restoreColorOnHover" a los eventos correspondientes de cada elemento "path"
            paths
               .on('click', this.changeColorOnClick)
               .on('mouseover', this.changeColorOnHover)
               .on('mouseout', this.restoreColorOnHover);

            // Agregar zoom al mapa
            const zoom = d3.zoom()
               .scaleExtent([1, 8]) // Definir los límites de zoom
               .on('zoom', this.zoomed); // Llamar a la función zoomed() cada vez que se haga zoom

            svg.call(zoom); // Llamar a la función zoom en el elemento SVG

            // Inicializar el estado del zoom
            this.currentZoom = 1;


         })
         .catch(error => {
            console.error(error);
         });
      const countries = this.$route.query.countries;
      if (countries) {
         const countryList = countries.split(",");
         const selectedCountries = countryList.join(", ");
      }

      // Añadir el controlador de eventos al control deslizante
      const yearSlider = document.getElementById('year-slider');
      yearSlider.addEventListener('input', (event) => {
         this.updateMap(event.target.value);
      });
   },
   methods: {
      // Función para cambiar el color de fondo de un elemento "path" a verde al hacer clic en él
      changeColorOnClick(event) {
         const path = event.target;

         if (path.classList.contains('selectedPath')) {
            // si ya está seleccionado, se quita el color
            path.style.fill = 'black';
            path.classList.remove('selectedPath');
            // se elimina el país de la lista de países seleccionados
            this.selectedStates = this.selectedStates.filter(state => state.id !== path.id);
         } else {
            // si no está seleccionado, se agrega el color
            path.style.fill = 'green';
            path.classList.add('selectedPath');
            // se agrega el país a la lista de países seleccionados
            this.selectedStates.push({ id: path.id, title: path.getAttribute('title') });
            console.log(this.selectedStates);
         }
      },

      // Función para cambiar el color de fondo de un elemento "path" a púrpura al pasar el mouse por encima
      changeColorOnHover(event) {
         const path = event.target;
         if (!path.classList.contains('selectedPath')) {
            path.style.fill = 'purple';
            document.getElementById("hover-value2").textContent = path.getAttribute('title');
         }
      },

      // Función para restaurar el color de fondo de un elemento "path" al dejar de pasar el mouse por encima
      restoreColorOnHover(event) {
         const path = event.target;

         if (!path.classList.contains('selectedPath')) {
            path.style.fill = 'black';
         }
      },
      // Funcion para vaciar la array y quitar el color de los paises seleccionados
      clearSelection() {
         // Vaciar el array de países seleccionados
         this.selectedStates.splice(0);

         // Deseleccionar todos los elementos del DOM que tengan la clase "selectedPath"
         const selectedPaths = document.querySelectorAll(".selectedPath");
         selectedPaths.forEach(element => {
            element.classList.remove("selectedPath");
            element.style.fill = "black";
         });
      },
      // Función para hacer zoom
      zoomIn() {
         this.currentZoom = Math.min(this.currentZoom / 0.9, 1.5); // Incrementar el factor de zoom actual y asegurarse de que no exceda el límite máximo
         d3.select('svg') // Seleccionar el elemento SVG
            .transition() // Agregar transición animada al zoom
            .duration(500) // Duración de la transición
            .attr("transform", "scale(" + this.currentZoom + ")"); // Aplicar la transformación de zoom
      },
      // Función para hacer zoom out
      zoomOut() {
         this.currentZoom = Math.max(this.currentZoom * 0.9, 0.5); // Decrementar el factor de zoom actual y asegurarse de que no sea menor que el límite mínimo
         d3.select('svg') // Seleccionar el elemento SVG
            .transition() // Agregar una transición suave al zoom
            .duration(500) // Duración de la transición (en milisegundos)
            .attr("transform", "scale(" + this.currentZoom + ")"); // Aplicar la transformación de zoom

      },
      // Función para hacer zoom con el scroll del ratón y draggear el mapa
      zoomed(event) {
         this.currentZoom = event.transform.k;
         d3.select("svg").attr("transform", event.transform); // Aplicar la transformación al elemento SVG actual
      },
      navigateToCharts() {
         const selectedCountries = this.selectedStates.map(state => state.title).join(",");
         this.$router.push({ name: "charts", query: { countries: selectedCountries } });
      },
      getDataFromAPI() {
         const apiUrl = `http://49.12.36.190/api/fertilizers-${selectedFertilizer.value}`;

         axios.get(apiUrl)
            .then(response => {
               const data = response.data;
               this.updateMapValues(data);
            })
            .catch(error => {
               console.error(error);
            });
      },

      updateMapValues(data) {
         const paths = document.querySelectorAll('path');
         const tooltip = document.createElement('div'); // Crea el elemento div para el tooltip
         tooltip.style.position = 'absolute';
         tooltip.style.backgroundColor = 'white';
         tooltip.style.border = '1px solid gray';
         tooltip.style.padding = '5px';
         tooltip.style.pointerEvents = 'none';
         tooltip.style.display = 'none'; // Oculta el tooltip por defecto
         document.body.appendChild(tooltip); // Agrega el tooltip al body

         paths.forEach(path => {
            const code = path.getAttribute('id');
            const value = data.find(item => item.code === code)?.amount ?? 0;
            path.setAttribute('amount', value);

            path.addEventListener('mouseover', () => {
               // Obtener posición del mouse y actualizar el contenido y la posición del tooltip
               const x = event.clientX;
               const y = event.clientY;
               tooltip.style.top = `${y}px`;
               tooltip.style.left = `${x}px`;
               tooltip.style.display = 'block'; // Muestra el tooltip
               tooltip.textContent = `${path.getAttribute('title')}: ${value}`;

            });

            path.addEventListener('mousemove', () => {
               // Actualiza la posición del tooltip mientras el mouse se mueve dentro del elemento "path"
               const x = event.clientX;
               const y = event.clientY;
               tooltip.style.top = `${y}px`;
               tooltip.style.left = `${x}px`;
            });

            path.addEventListener('mouseout', () => {
               // Oculta el tooltip cuando el mouse sale del elemento "path"
               tooltip.style.display = 'none';
            });
         });
         this.updateMapColors();
      },
      createLegend(colorScale, colors) {
         // Elimina la leyenda anterior si existe
         const existingLegend = document.getElementById('legend-container');
         if (existingLegend) {
            existingLegend.remove();
         }

         const legendContainer = document.createElement('div');
         legendContainer.setAttribute('id', 'legend-container');
         legendContainer.style.display = 'flex';
         legendContainer.style.flexDirection = 'row';
         legendContainer.style.alignItems = 'center';
         legendContainer.style.justifyContent = 'center';
         legendContainer.style.marginTop = '10px';

         colors.forEach((color, index) => {
            const colorBox = document.createElement('div');
            colorBox.style.backgroundColor = color;
            colorBox.style.width = '20px';
            colorBox.style.height = '20px';
            colorBox.style.margin = '0 5px';

            const rangeText = document.createElement('span');
            rangeText.style.marginLeft = '5px';
            rangeText.style.marginRight = '10px';
            const range = colorScale.invertExtent(color);
            // Caso especial para el primer rango (0.00 - 0.00)
            if (index === 0) {
               rangeText.textContent = `${range[0].toFixed(2)} - ${range[0].toFixed(2)}`;
            } else {
               rangeText.textContent = `${range[0].toFixed(2)} - ${range[1].toFixed(2)}`;
            }

            const legendItem = document.createElement('div');
            legendItem.style.display = 'flex';
            legendItem.style.alignItems = 'center';
            legendItem.appendChild(colorBox);
            legendItem.appendChild(rangeText);

            legendContainer.appendChild(legendItem);
         });

         // Agrega la leyenda al final del body
         document.body.appendChild(legendContainer);
      },
      updateMapColors() {
         const paths = document.querySelectorAll('path');
         const colors = [
            '#F5E1F7',
            '#E6B8E6',
            '#D7A3D3',
            '#C68FC6',
            '#B67AB6',
            '#A666A3',
            '#965291',
            '#854D80',
            '#73386E',
            '#62245C'

         ];
         const amounts = Array.from(paths, path => Number(path.getAttribute('amount')));
         const maxAmount = Math.max(...amounts);
         const colorScale = d3.scaleQuantile()
            .domain(amounts.filter(amount => amount > 0)) // Excluye el valor 0.00 de la escala
            .range(colors.slice(1)); // Excluye el primer color del rango, ya que se manejará por separado

         paths.forEach(path => {
            const amount = Number(path.getAttribute('amount'));
            const color = amount === 0 ? colors[0] : colorScale(amount); // Usa el primer color del arreglo para el rango 0.00 - 0.00
            path.style.fill = color;
         });

         // Crear leyenda
         this.createLegend(colorScale, colors);
      },

      updateFertilizerType(event) {
         selectedFertilizer.value = event.target.value;
         this.getDataFromAPI();
      },

      addLegend() {
         // Elimina la leyenda anterior si existe
         const existingLegend = document.getElementById('map-legend');
         if (existingLegend) {
            existingLegend.remove();
         }

         // A continuación, el código existente para agregar la leyenda
         const legend = L.control({ position: 'bottomright' });

         legend.onAdd = () => {
            const div = L.DomUtil.create('div', 'info legend');
            div.id = 'map-legend'; // Agrega un ID para que podamos seleccionarlo y eliminarlo fácilmente
            const grades = this.legendGrades;
            const labels = [];

            for (let i = 0; i < grades.length; i++) {
               labels.push(
                  '<i style="background:' +
                  this.getColor(grades[i] + 1) +
                  '"></i> ' +
                  grades[i] +
                  (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+')
               );
            }

            div.innerHTML = labels.join('');
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
         }, 1000); // Cambia cada 1000 milisegundos (1 segundo)
      }

// const playButton = document.getElementById('play-button');
//       playButton.addEventListener('click', playYears);



   }
};


</script>


<style scoped>
.prio {
   position: relative;
   z-index: 1;
   margin-right: auto;
   width: fit-content;
   height: fit-content;
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
   margin-right: auto;
   width: 2%;
   height: 2%;
}

.draggeable {
   cursor: move;
}

.selected {
   fill: green;
}

path {
   fill: black;
   transition: fill 0.5s ease-in-out;
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
