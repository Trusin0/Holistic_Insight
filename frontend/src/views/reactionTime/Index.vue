<template>
  <div class="reaction-time">
    <!-- 初始界面 -->
    <div v-if="step === 1" class="initial-screen">
      <p>{{ message }}</p>
      <button @click="start">开始</button>
    </div>

    <!-- 等待界面 -->
    <div v-if="step === 2" class="waiting-screen" @click="handleClick">
      <p>请等待</p>
    </div>

    <!-- 点击界面 -->
    <div v-if="step === 3" class="click-screen" @click="handleClick">
      <p>点击！</p>
    </div>

    <!-- 结果界面 -->
    <div v-if="step === 4" class="result-screen" @click="handleClick">
      <p>反应时间：{{ reactionTime }}ms</p>
    </div>

    <!-- 错误界面 -->
    <div v-if="step === 5" class="error-screen" @click="handleClick">
      <p>太快了</p>
    </div>

    <!-- 结算界面 -->
    <div v-if="step === 6" class="settlement-screen" @click="handleClick">
      <p>测试结束</p>
      <p>平均时间：{{ allTime / 5 }}ms</p>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      step: 1, // 初始界面
      message: '当屏幕变为绿色时，请点击屏幕',
      reactionTime: 0,
      timer: null,
      startTime: null,
      chances: 5, // 需要做的测试次数
      allTime: 0 // 总时间
    }
  },
  methods: {
    start () {
      this.step = 2 // 进入等待界面
      // 随机等待时间
      const waitTime = Math.random() * 4000 + 2000 // 2到4秒之间
      this.timer = setTimeout(() => {
        this.step = 3 // 进入点击界面
        this.startTime = Date.now() // 记录开始时间
      }, waitTime)
    },
    handleClick () {
      if (this.step === 2) {
        this.step = 5 // 进入错误界面
        clearTimeout(this.timer) // 清除等待界面的定时器
      } else if (this.step === 3) {
        const endTime = Date.now()
        this.reactionTime = endTime - this.startTime
        this.step = 4 // 进入结果界面
        clearTimeout(this.timer) // 清除等待界面的定时器
      } else if (this.step === 4) {
        if (this.chances !== 0) {
          this.chances-- // 减少测试次数
          this.allTime = this.allTime + this.reactionTime // 追加总时间
          this.start() // 开始下一轮测试
        } else {
          this.allTime = this.allTime + this.reactionTime // 追加总时间
          this.step = 6 // 进入结算界面
        }
      } else if (this.step === 5) {
        this.start() // 开始下一轮测试
      }
    }
  },
  beforeDestroy () {
    clearTimeout(this.timer) // 组件销毁时清除定时器
  }
}
</script>

<style scoped>
.reaction-time {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 500px;
  text-align: center;
  cursor: pointer;
}

.initial-screen,
.waiting-screen,
.click-screen,
.result-screen,
.settlement-screen,
.error-screen {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.settlement-screen,
.result-screen,
.initial-screen {
  background-color: #3498db; /* 蓝色背景 */
}

.waiting-screen {
  background-color: #e74c3c; /* 红色背景 */
}

.click-screen {
  background-color: #2ecc71; /* 绿色背景 */
}

.error-screen {
  background-color: #e74c3c; /* 红色背景 */
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
