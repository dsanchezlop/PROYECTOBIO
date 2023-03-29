<template>
  <div class="app">
    <h1>Interactive map</h1>
    <SVGMap></SVGMap>
  </div>
  
</template>

<script>
import SVGMap from '@/components/SVGMap.vue';

export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    SVGMap
  }
};

</script>

<style>
.app {
  height: 100vh;
}
</style>
