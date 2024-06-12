<template>
  <div class="hello">
    <img src="../assets/logo.png" style="width: 300px; height: auto;">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Holistic Insight， 测试您的各项能力',
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  display: flex;
  flex-direction: column; /* 使图片和文字在垂直方向排列 */
  justify-content: center; /* 在主轴（垂直方向）上居中 */
  align-items: center; /* 在交叉轴（水平方向）上居中 */
  height: 100vh; /* 使容器占满整个视口高度 */
  text-align: center; /* 使文本在行内居中 */
}

.hello img {
  max-width: 100%; /* 确保图片不会超出容器的宽度 */
  height: auto; /* 保持图片的纵横比 */
}
</style>
