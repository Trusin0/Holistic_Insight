<template>
  <div class="footer-bar-wrap">
    <div class="footer-bar">
      <div class="line"></div>
      <p>Sun-Yat-Sen University | School of Computer Science and Engineering </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FooterBar',
  data () {
    return {
      msg: 'This is the FooterBar component'
    }
  }
}
</script>

<style scoped>
.footer-bar-wrap {
  padding: 20px;
  text-align: center;
  background-color: #333;
  color: white;
  bottom: 0;
  width: 100%;
  height: 20px; /* 调整底部导航栏的高度为 20px */
}
.footer-bar {
  margin: 0 auto;
}
.line {
  height: 1px;
  width: 100%;
  margin: 0 auto;
  background-color: #333;
}
p {
  margin:0;
  font-size: 16px;
  font-weight: bold;
}
</style>
