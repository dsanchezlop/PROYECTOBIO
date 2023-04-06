<template>
   <button class="button-zoom" @click="zoomIn">+</button>
   <button class="button-zoom" @click="zoomOut">-</button>
   <br>
   <button class="button-container" @click="clearSelection"> Clear Selection </button>

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
   <div ref="chart">
   </div>
</template>


<script>
import { ref } from 'vue';
import * as d3 from "d3";

export default {
   data() {
      return {
         selectedStates: ref([]),
         currentZoom: 1
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
            const importedNode = document.importNode(data.documentElement, true);
            svg.node().appendChild(importedNode);

            // Obtener todos los elementos "path" del SVG
            const paths = svg.selectAll('path');

            // Asignar las funciones "changeColorOnClick", "changeColorOnHover" y "restoreColorOnHover" a los eventos correspondientes de cada elemento "path"
            paths
               .on('click', this.changeColorOnClick)
               .on('mouseover', this.changeColorOnHover)
               .on('mouseout', this.restoreColorOnHover)               ;

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
      }
   }
}
</script>


<style scoped>
.prio{
   position: relative;
   z-index: 1;
   margin-right: auto;
   width: fit-content;
   height: fit-content;
}

h2, h3, h4 {
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
</style>
