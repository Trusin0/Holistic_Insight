
<!-- 这个文件是Vue.js应用程序的起点，它为整个应用程序提供了一个基本的布局和样式框架。
     在App.vue中通常添加全局的样式和逻辑，以及配置应用程序的路由等。-->

<template>
  <div id="app">
    <top-bar></top-bar>
    <div class="main-content">
      <router-view/>
    </div>
    <footer-bar></footer-bar>
  </div>
</template>

<script>

import TopBar from '@/components/TopBar.vue'
import FooterBar from '@/components/FooterBar.vue'
import Dashboard from '@/components/Dashboard.vue'

export default {
  name: 'App',
  components: {
    TopBar,
    FooterBar
  }
}
</script>

<style scoped>
.main-content {
  //padding-top: 100px;
  //padding-bottom: 400px; /* 给footer-bar预留空间 */
}
</style>
