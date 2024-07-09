<template>
  <div class="index_pages">
    <img src="../../assets/logo.png" style="width: 300px; height: auto;">
    <h1>{{ msg }}</h1>
    <div class="game-list">
      <el-row justify="space-evenly">
        <el-col :xs="24" :sm="12" :md="8" :lg="8" :xl="8" v-for="(item, index) of gameList" :key="index">
          <game-item :title="item.title" :intro="item.intro" :path="item.path"></game-item>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import GameItem from './components/GameItem.vue'
import { gameList } from './config/GameList'

export default {
  name: 'Index',
  data () {
    return {
      gameList,
      msg: 'Holistic Insight，测试您的各项能力'
    }
  },
  components: {
    GameItem
  }
}
</script>

<style scoped>
.index_pages {
  display: flex;
  flex-direction: column; /* 使图片和文字在垂直方向排列 */
  justify-content: center; /* 在主轴（垂直方向）上居中 */
  align-items: center; /* 在交叉轴（水平方向）上居中 */
  height: 200vh; /* 使容器占满整个视口高度 */
  text-align: center; /* 使文本在行内居中 */
}

.index_pages img {
  max-width: 100%; /* 确保图片不会超出容器的宽度 */
  height: auto; /* 保持图片的纵横比 */
}

.game-list {
  width: 80%;
  margin: 0 auto; /* 使游戏列表居中 */
}
</style>
