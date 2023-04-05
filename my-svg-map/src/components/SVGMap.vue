<template>
   <button class="button-zoom" @click="zoomIn">+</button>
   <button class="button-zoom" @click="zoomOut">-</button>
   <br>
   <button class="button-container" @click="clearSelection"> Clear Selection </button>

   <div>
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
      <div style="display:flex; text-align: center; align-items: center;">
         <h2>Hovered Country:</h2>
         <h3 style="color: black" id="hover-value2">Move your mouse</h3>
      </div>
   </div>
   <div ref="chart">
      <svg></svg>
   </div>
</template>


<script>
import { ref } from 'vue';
import * as d3 from "d3";

export default {
   data() {
      return {
         selectedStates: ref([])
      }
   },
   mounted() {
      const svg = d3.select(this.$refs.chart)
         .append("svg")
         .attr("width", "1009.6727")
         .attr("height", "665.96301");

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
               .on('mouseout', this.restoreColorOnHover);
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
      }
   }
}
</script>


<style scoped>
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
