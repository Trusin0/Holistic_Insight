<template>
  <div class="game-item" @click="$router.push(path)">
    <img :src=icon style="width: 100px; height: auto;" >
    <h4>{{ title }}</h4>
    <span>{{ intro }}</span>
  </div>
</template>

<script>
export default {
  props: {
    icon: String,
    title: String,
    intro: {
      type: String,
      default: ''
    },
    path: {
      type: String,
      default: '/index'
    }
  }
}
</script>

<style scoped>
.game-item {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
  width: 260px;
  height: 260px;
  color: #333;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* 替换为具体的阴影样式 */
  border-radius: 10px;
  margin: 20px auto 0 auto;
  cursor: pointer;
  top: 0;
  transition: transform .5s;
}

.game-item:hover {
  transform: translate(0, -10px);
}

.game-item h4 {
  font-size: 24px;
}

.game-item span {
  font-size: 18px;
}

@media screen and (max-width: 480px) {
  .game-item {
    width: 100%;
    border-radius: 0; /* 取消边框半径 */
  }
}

</style>
