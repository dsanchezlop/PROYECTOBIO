<template>
   <button class="button-zoom" @click="zoomIn">+</button>
   <button class="button-zoom" @click="zoomOut">-</button>
   <br>
   <button class="button-container" @click="clearSelection"> Clear Selection </button>

   <div>
      <h2> Selected Countries :</h2>
      <div style="display:inline">
         <h4 style="display:inline; margin:10px;" v-for="state in selectedStates" :key="state.id"> {{ state.id }} :
            {{ state.title }} </h4>
      </div>
      <div style="display:flex; text-align: center; align-items: center;">
         <h2>Hovered Country:</h2>
         <h3 style="color: black"> {{ hoverValue }} </h3>
      </div>
   </div>
   <div ref="chart">
      <svg></svg>
   </div>
</template>

<script>
import { ref } from 'vue';
import * as d3 from "d3";

const hoverValue = ref("Mouse your mouse");
const selectedStates = ref([]);
const zoomLevel = ref(1);
const dragInfo = ref(null);

export default {
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

        // Asignar la función "changeColorOnClick" al evento "click" de cada elemento "path"
        paths.on('click', changeColorOnClick);
      })
      .catch(error => {
        console.error(error);
      });
  },
};

// Función para cambiar el color de fondo de un elemento "path" a verde al hacer clic en él
function changeColorOnClick(event) {
  const path = event.target;

  if (path.classList.contains('selectedPath')) {
    // si ya está seleccionado, se quita el color
    path.style.fill = 'black';
    path.classList.remove('selectedPath');
    // se elimina el país de la lista de países seleccionados
    selectedStates.value = selectedStates.value.filter(state => state.id !== path.id);
  } else {
    // si no está seleccionado, se agrega el color
    path.style.fill = 'green';
    path.classList.add('selectedPath');
    // se agrega el país a la lista de países seleccionados
    selectedStates.value.push({id: path.id, title: path.getAttribute('title')});
  }
}
</script>

<style scoped>
@keyframes slowchange {
   to {
      fill: indianred;
   }
}

@keyframes hoverChange {
   to {
      fill: purple;
   }
}

path {
   fill: black;
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

.logo {
   height: 6em;
   padding: 1.5em;
   will-change: filter;
}

.logo:hover {
   filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
   filter: drop-shadow(0 0 2em #42b883aa);
}

.map-container {
   width: 100vw;
   /* ancho al 100% de la ventana */
   /* height: 100vh; altura al 100% de la ventana */
   display: flex;
   justify-content: center;
   /* centro horizontal */
   align-items: center;
   /* centro vertical */
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
