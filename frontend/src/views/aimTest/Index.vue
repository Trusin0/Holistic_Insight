<template>
  <div class="aim-test">
    <!-- 初始界面 -->
    <div v-if="!gameStarted" class="initial-screen">
      <p>{{ message }}</p>
      <button @click="start">开始</button>
    </div>

    <!-- 游戏界面 -->
    <div v-else id="gameArea" @click="clickBall" ref="gameAreaRef">
      <p v-if="!gameOver">剩余 {{ ballsRemaining }} 球</p>
      <div v-if="ball" :style="{ left: ball.x + 'px', top: ball.y + 'px' }" class="ball"></div>
    </div>

    <!-- 结果界面 -->
    <div v-if="gameOver" class="result-screen">
      <p>每个目标平均用时：{{ averageTime }}ms</p>
      <button @click="saveScore">保存分数</button>
      <button @click="start">再试一次</button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      gameStarted: false,
      message: '尽快点击小球吧！',
      ballsRemaining: 30, // 初始球的数量
      ball: null, // 当前球的信息
      startTime: 0,
      endTime: 0,
      totalClickTime: 0,
      gameOver: false,
      averageTime: 0 // 添加此行来存储平均时间
    }
  },
  methods: {
    start () {
      console.log('Start game') // Debugging
      this.gameStarted = true
      this.gameOver = false
      this.ballsRemaining = 30 // 重置球的数量
      this.totalClickTime = 0 // 重置点击时间
      this.startTime = new Date().getTime() // 重置开始时间
      this.$nextTick(() => {
        this.createBall() // 确保DOM更新完成后再调用createBall
      })
    },
    createBall () {
      console.log('Create ball') // Debugging
      const gameArea = this.$refs.gameAreaRef
      const rect = gameArea.getBoundingClientRect()
      const width = rect.width
      const height = rect.height

      this.ball = {
        id: Date.now(), // 使用时间戳作为唯一标识符
        x: Math.random() * (width - 100), // 球的宽度为100px
        y: Math.random() * (height - 100), // 球的高度为100px
        radius: 50 // 球的半径为50px
      }

      this.startTime = new Date().getTime() // 设置开始时间
    },
    clickBall (e) {
      console.log('Click ball') // Debugging
      if (!this.ball) return // 如果没有球，直接返回

      const gameArea = this.$refs.gameAreaRef
      const rect = gameArea.getBoundingClientRect()
      const offsetX = e.clientX - rect.left // 获取相对于 gameArea 的 offsetX
      const offsetY = e.clientY - rect.top // 获取相对于 gameArea 的 offsetY

      console.log('Clicked at:', offsetX, offsetY) // 输出点击位置

      const ballCenterX = this.ball.x + this.ball.radius
      const ballCenterY = this.ball.y + this.ball.radius

      console.log('Ball center:', ballCenterX, ballCenterY) // 输出球的中心位置

      // 计算点击位置与球心的距离
      const distance = Math.sqrt(Math.pow(offsetX - ballCenterX, 2) + Math.pow(offsetY - ballCenterY, 2))

      if (distance <= this.ball.radius) {
        console.log('Ball clicked:', this.ball) // Debugging
        this.endTime = new Date().getTime()
        this.totalClickTime += this.endTime - this.startTime

        if (this.ballsRemaining > 0) {
          this.createBall() // 创建新球
          this.ballsRemaining--
        } else {
          this.ball = null // 清空球的信息
          this.gameOver = true
          this.averageTime = (this.totalClickTime / 30).toFixed(2) // 计算平均时间并保留两位小数
        }
      } else {
        console.log('Missed the ball') // Debugging
      }
    },
    saveScore () {
      // 保存分数逻辑
    }
  }
}
</script>

<style>
#gameArea {
  position: relative;
  width: 100%;
  height: 700px;
  background-color: #3498db;
}

.aim-test {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 700px;
  text-align: center;
  cursor: pointer;
}

.result-screen,
.initial-screen {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: #3498db;
}

.ball {
  position: absolute;
  width: 100px; /* 直径为100px */
  height: 100px; /* 直径为100px */
  background-color: white;
  border-radius: 50px; /* 半径为50px */
}

button {
  background-color: #f1c40f;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #f39c12;
}

p {
  font-size: 40px;
  animation: textFadeIn .5s linear;
  color: #ffffff;
}
</style>
