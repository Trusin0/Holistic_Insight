<template>
  <div class="aim-test">
    <!-- 初始界面 -->
    <div v-if="!gameStarted" class="initial-screen">
      <p>{{ message }}</p>
      <button @click="start">开始</button>
    </div>

    <!-- 游戏界面 -->
    <div v-else id="gameArea" @click="clickBall">
      <p>剩余 {{ ballsRemaining }} 球</p>
      <div v-for="ball in balls" :key="ball.id" :style="{ left: ball.x + 'px', top: ball.y + 'px' }" class="ball"></div>
    </div>

    <!-- 结果界面 -->
    <div v-if="gameOver">
      <p>每个目标平均用时：{{ averageTime }}ms</p>
      <button @click="saveScore">保存分数</button>
      <button @click="startGame">再试一次</button>
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
      balls: [],
      startTime: 0,
      endTime: 0,
      totalClickTime: 0,
      gameOver: false
    }
  },
  methods: {
    start () {
      this.gameStarted = true
      this.ballsRemaining = 30 // 重置球的数量
      this.createBalls()
    },
    createBalls () {
      const gameArea = this.$el.querySelector('#gameArea')
      const width = gameArea.offsetWidth
      const height = gameArea.offsetHeight

      for (let i = 0; i < this.ballsRemaining; i++) {
        const ball = {
          id: i,
          x: Math.random() * (width - 20), // 球的宽度为20px
          y: Math.random() * (height - 20) // 球的高度为20px
        }
        this.balls.push(ball)
      }
    },
    clickBall (e) {
      const ball = this.balls.find(b =>
        Math.sqrt(Math.pow(e.clientX - b.x, 2) + Math.pow(e.clientY - b.y, 2)) < 10 // 点击范围为10px
      )

      if (ball) {
        this.endTime = new Date().getTime()
        this.totalClickTime += this.endTime - this.startTime
        this.startTime = this.endTime
        this.balls.splice(this.balls.indexOf(ball), 1)
        this.ballsRemaining--

        if (this.ballsRemaining === 0) {
          this.gameOver = true
          this.averageTime = this.totalClickTime / this.balls.length
        }
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
  height: 600px;
  background-color: #f0f0f0;
}

.initial-screen {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.ball {
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: white;
  border-radius: 10px;
}
</style>
