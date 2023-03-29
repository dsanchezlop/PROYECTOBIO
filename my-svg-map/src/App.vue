<template>
    <h1>FertImpact</h1>
    <div>
    <router-link to="/"> Home </router-link>
    <router-link to="/map"> Maps </router-link>
    <router-link to="/map_faun"> Fauna maps </router-link>
    <router-link to="/database"> Database </router-link>
    <router-link to="/login"> Login </router-link>
    <router-link to="/register"> Register </router-link>
    <router-link to="/profile"> Profile </router-link>
    <router-link to="/logout"> Logout </router-link>
  </div>
  <router-view/>
  
</template>

<!-- <script>
import SVGMap from '@/components/SVGMap.vue';

export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-unused-components
    SVGMap
  }
};

</script> -->

<style>
/* .app {
  height: 100vh;
} */
</style>
