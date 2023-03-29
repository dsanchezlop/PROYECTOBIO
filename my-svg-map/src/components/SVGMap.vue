<template>
  <div class="svg-map">
    <svg :width="width" :height="height">
      <g>
        <image :href="mapPath" />
        <path
          v-for="(country, index) in countries"
          :key="index"
          :d="country.path"
          :fill="country.fill"
          @mouseover="handleCountryHover(index)"
          @mouseleave="handleCountryLeave(index)"
        />
      </g>
    </svg>
  </div>
</template>

<script>
import mapPath from '@/assets/world.svg';
import countriesData from '@/assets/countries.json';

export default {
  name: 'SVGMap',
  data() {
    return {
      width: 1010,
      height: 666,
      mapPath,
      countries: countriesData.map((country) => ({
        ...country,
        fill: '#ccc'
      }))
    };
  },
  methods: {
    handleCountryHover(index) {
      this.countries[index].fill = 'blue';
    },
    handleCountryLeave(index) {
      this.countries[index].fill = '#ccc';
    }
  }
};
</script>

<style scoped>
.svg-map {
  display: block;
  margin: 0 auto;
  max-width: 100%;
}
</style>
