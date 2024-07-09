<template>
  <div>
    <!-- 初始界面 -->
    <div v-if="stage === 0" class="initial-screen">
      色觉敏感度测试
      <button @click="resetGame">GO</button>
    </div>

    <!--  游戏界面  -->
    <div v-if="stage === 1" class="game-screen">
      <p class="game-text">得分: {{ score }}     剩余时间: {{ timer }} 秒</p>
      <div class="grid" :style="gridStyle">
        <div
          v-for="(color, index) in colors"
          :key="index"
          class="color-box"
          :style="{ backgroundColor: color }"
          @click="checkAnswer(index)"
        ></div>
      </div>
    </div>
    <div v-if="stage === 2" class="initial-screen">
      <p>游戏结束</p>
      <p>你的分数是: {{ score }}</p>
      <button @click="resetGame()">重新开始</button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      baseColor: '',
      colors: [],
      differentColorIndex: null,
      stage: 0,
      timer: 60,
      interval: null,
      score: 0,
      gridSize: 2
    }
  },
  beforeDestroy () {
    clearInterval(this.interval)
  },
  computed: {
    gridStyle () {
      return {
        gridTemplateColumns: `repeat(${this.gridSize}, 1fr)`,
        gridTemplateRows: `repeat(${this.gridSize}, 1fr)`
      }
    }
  },
  methods: {
    // 游戏状态初始化
    resetGame () {
      this.stage = 1
      this.timer = 60
      this.score = 0
      this.gridSize = 2
      this.setGrip()
      this.startTimer()
    },
    // 重新设置grid
    setGrip () {
      this.baseColor = this.generateColor()
      this.differentColorIndex = Math.floor(Math.random() * this.gridSize * this.gridSize)
      this.colors = Array(this.gridSize * this.gridSize).fill(this.baseColor)
      this.colors[this.differentColorIndex] = this.generateColor(true)
    },
    generateColor (different = false) {
      if (!different) {
        return `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`
      } else {
        // Create a subtle difference based on level
        let [baseRed, baseGreen, baseBlue] = this.baseColor.match(/\d+/g).map(Number)
        let adjust = Math.max(40 - this.score, 23) // Difference factor decreases as level increases
        adjust += Math.random() * 5
        baseRed = Math.min(baseRed + adjust, 256)
        baseGreen = Math.min(baseGreen + adjust, 256)
        baseBlue = Math.min(baseBlue + adjust, 256)

        return `rgb(${baseRed}, ${baseGreen}, ${baseBlue})`
      }
    },
    checkAnswer (index) {
      if (index === this.differentColorIndex) {
        this.score++
        if (this.score === 1) {
          this.gridSize = 3
        } else if (this.score === 2) {
          this.gridSize = 4
        } else if (this.score === 3 || this.score === 4) {
          this.gridSize = 5
        } else if (this.score === 5 || this.score === 6) {
          this.gridSize = 6
        } else if (this.score >= 7 && this.score <= 9) {
          this.gridSize = 7
        } else if (this.score >= 10 && this.score <= 15) {
          this.gridSize = 8
        } else if (this.score >= 16) {
          this.gridSize = 9
        }
        this.setGrip()
      }
    },
    startTimer () {
      this.interval = setInterval(() => {
        if (this.timer > 0) {
          this.timer--
        } else {
          this.stage = 2
          clearInterval(this.interval)
        }
      }, 1000)
    }
  }
}
</script>

<style scoped>
/* 初始界面样式 */
.initial-screen {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh; /* 使初始屏幕填满视窗的高度 */
  background-color: #A7D2FCFC; /* 一个明亮的背景颜色 */
  text-align: center;
  padding: 20px; /* 添加一些内边距 */
  font-size: 70px; /* 增大字体大小，更易阅读 */
  color: #FFFFFFFC; /* 白色文字 */
  margin-bottom: 80px; /* 添加下边距 */
  font-weight: bold; /* 字体加粗 */
}

.initial-screen button {
  padding: 10px 15px; /* 按钮内边距 */
  font-weight: bold; /* 字体加粗 */
  font-size: 40px; /* 适中的按钮文本大小 */
  color: #FFFFFFFC; /* 白色文字 */
  background-color: #3FB1FFFC; /* 按钮背景颜色 */
  border: none;
  border-radius: 10px; /* 圆角边框 */
  cursor: pointer; /* 显示手型光标表示可点击 */
  transition: background-color 0.2s; /* 过渡效果让按钮的变化更平滑 */
}

.initial-screen button:hover {
  background-color: #3580E7FF; /* 鼠标悬停时按钮颜色加深 */
}

/* 游戏界面样式 */
.game-screen {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 110vh; /* 使初始屏幕填满视窗的高度 */
  background-color: #A7D2FCFC; /* 一个明亮的背景颜色 */
  color: #333333; /* 文本颜色 */
  text-align: center;
  padding: 20px; /* 添加一些内边距 */
}

.game-text {
  font-size: 20px;
  margin-bottom: 10px;
  color: rgba(243, 158, 158, 0.99); /* 白色文字 */
}
.grid {
  display: grid;
  width: 400px;  /* 固定网格的宽度 */
  height: 400px; /* 固定网格的高度 */
  //margin: auto;  /* 水平居中 */
  gap: 10px;
  position: relative;  /* 相对定位 */
  top: 50%; /* 垂直居中 */
  transform: translateY(-100%); /* 通过变换确保垂直居中 */
}

.color-box {
  cursor: pointer;
}
</style>
