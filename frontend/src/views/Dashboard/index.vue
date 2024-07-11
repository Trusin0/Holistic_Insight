<template>
  <div id="app">
    <TestDashboard />
  </div>
</template>

<script>
import TestDashboard from './TestDashboard.vue';

export default {
  name: 'App',
  components: {
    TestDashboard
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
