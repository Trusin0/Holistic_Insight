<template>
  <footer>
    <p>Sun-Yat-Sen University</p>
  </footer>
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
  footer {
    padding: 20px;
    text-align: center;
    background-color: #333;
    color: white;
    position: absolute;
    bottom: 0;
    width: 100%;
  }
  p {
    margin: 0;
    font-size: 16px;
    font-weight: bold;
  }
</style>
