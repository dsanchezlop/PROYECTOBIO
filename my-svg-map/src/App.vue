<template>
    <div style="position: absolute; top:1em;left:1em">
    <router-link to="/"> Home </router-link>
    <router-link to="/map"> Maps </router-link>
  </div>
  <router-view/>
  
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
