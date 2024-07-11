<template>
  <div id="app" class="game-container">
    <!-- 游戏开始界面 -->
    <div v-show="gameState === 'start'" class="start-screen">
      <h1>数字记忆</h1>
      <p>测试您对数字序列的记忆能力，出现的数字量会逐级递增</p>
      <button @click="startGame" class="start-button">开始</button>
    </div>

    <!-- 游戏进行界面 -->
    <div v-show="gameState === 'play'" class="play-screen">
      <div v-if="numbersShown" class="numbers-display">
        <!-- 数字显示在同一行，增大字体大小 -->
        <span v-for="number in shownNumbers" :key="number" class="number">{{ number }}</span>
      </div>
      <div class="timer-container" v-if="numbersShown">
        <div class="timer-bar" :style="timerBarStyle"></div> <!-- 进度条 -->
      </div>
      <button v-if="!numbersShown" @click="showNumbers" class="show-numbers-button">展示本关数字</button>
    </div>

    <!-- 用户输入界面 -->
    <div v-show="gameState === 'input'" class="input-screen">
      <!-- 输入框单独一行 -->
      <input v-model="userInput" class="input-field" placeholder="Enter the numbers you saw" @input="formatInput" />
      <!-- 提交按钮单独一行 -->
      <div class="submit-container">
        <button @click="submitAnswer" class="submit-button">提交</button>
      </div>
    </div>

    <!-- 游戏结果界面 -->
    <div v-show="gameState === 'result'" class="result-screen">
      <h2 v-if="isCorrect">数字序列正确!</h2>
      <h2 v-else>数字序列错误!</h2>
      <p>正确序列: {{ correctNumbers }}</p>
      <p>你的答案: {{ userInput }}</p>
      <button @click="restartGame" class="restart-button">重新开始</button>
      <button @click="saveScore" class="save-button">保存分数</button>
    </div>

    <div v-show="gameState === 'level-up'" class="level-up-screen">
      <h2>Level Up!</h2>
      <p>当前通关等级: {{ level }}</p>
      <button @click="nextLevel" class="next-level-button">下一关</button>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      gameState: 'start',
      numbers: [],
      shownNumbers: [],
      numbersShown: false,
      userInput: '',
      correctNumbers: '',
      level: 1,
      isCorrect: null,
      timer: null,
      timerDuration: 3000, // 计时器持续时间3秒
      elapsedTime: 0, // 已过去的时间
    };
  },
  computed: {
    timerBarStyle() {
      return {
        width: (100 * (1 - this.elapsedTime / this.timerDuration)) + '%',
      };
    },
  },
  methods: {
    startGame() {
      if (this.level === 1) {

        this.generateNumbers();
        this.gameState = 'play';
      }
    },
    generateNumbers() {
      this.numbers = [];
      for (let i = 0; i < this.level; i++) {
        this.numbers.push(Math.floor(Math.random() * 10));
      }
      this.correctNumbers = this.numbers.join('');
      this.numbersShown = false; // 重置numbersShown以确保数字只在showNumbers方法中显示
    },
    showNumbers() {
      this.numbersShown = true;
      this.shownNumbers = this.numbers.slice();
      this.startTimer(); // 开始计时
    },
    startTimer() {
      this.timer = setInterval(() => {
        if (this.elapsedTime < this.timerDuration) {
          this.elapsedTime += 100; // 每次增加100ms，更新进度条
        } else {
          clearInterval(this.timer);
          this.gameState = 'input';
        }
      }, 100);
    },
    resetTimer() {
      if (this.timer) {
        clearInterval(this.timer); // 清除计时器
        this.timer = null; // 重置timer
      }
      this.elapsedTime = 0; // 重置已过去的时间
      // 根据需要重置其他相关的状态或变量
    },
    formatInput(event) {
      this.userInput = event.target.value.replace(/[^0-9]/g, '');
    },
    submitAnswer() {
      const trimmedInput = this.userInput.replace(/\s+/g, '');
      if (trimmedInput === this.correctNumbers) {
        this.gameState = 'level-up';
      } else {
        this.isCorrect = false;
        this.gameState = 'result';
        this.userInput = trimmedInput; // 保存用户最终的输入，不含空格
      }
      this.resetTimer();
    },
    nextLevel() {
      this.level++;
      this.generateNumbers();
      this.gameState = 'play';
      this.userInput = '';
    },
    restartGame() {
      this.gameState = 'start';
      this.level = 1;
      this.userInput = '';
      this.numbers = [];
      this.shownNumbers = [];
      this.numbersShown = false;
      this.correctNumbers = '';
      clearTimeout(this.timer);
      this.elapsedTime = 0;
    },
    saveScore () {
      const currentTime = new Date().getTime() // 记录当前时间
      this.$http.get('http://127.0.0.1:8000/api/game/save_game_data?game_name=number&level=' + (this.level) + '&usr_name=' + this.$store.state.userInfo.username + '&play_time=' + currentTime)
        .then(response => {
          var res = JSON.parse(response.bodyText)
          if (res.message === 'Save successful') {
            this.$message.success('新增成绩成功')
          } else {
            this.$message.error('新增成绩失败，请重试')
            console.log(res.message)
          }
        })
    }
  },
};
</script>

<style scoped>
.game-container {
  font-family: 'Arial', sans-serif;
  text-align: center;
  margin: 0 auto;
  padding: 20px;
  max-width: 100%; /* 宽度调整为100% */
  height: 100vh; /* 高度调整为视窗高度的90% */
  background-color: #3497da; /* 背景颜色调整为蓝色 */
  color: white; /* 文字颜色调整为白色 */
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.start-screen h1,
.start-screen p,
.play-screen .numbers-display,
.show-numbers-button,
.input-field,
.submit-button,
.result-screen h2,
.restart-button,
.save-button {
  font-size: 2em; /* 所有文本大小放大 */
}

.start-screen h1 {
  color: white; /* 标题颜色调整为白色 */
  margin-bottom: 0.5em;
}

.start-screen p {
  margin-bottom: 1.5em;
}

.start-button {
  background-color: #4CAF50;
  color: white;
  padding: 20px 40px; /* 按钮大小放大 */
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 1.2em; /* 按钮文字大小 */
}

.start-button:hover {
  background-color: #45a049;
}

.play-screen .numbers-display {
  margin-bottom: 1em;
}
.play-screen{
  width: 50%;
}

.show-numbers-button {
  background-color: #f0ad4e;
  color: white;
  padding: 15px 30px; /* 按钮大小放大 */
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin-bottom: 1em;
  transition: background-color 0.3s ease;
}

.show-numbers-button:hover {
  background-color: #ec971f;
}

.input-field {
  padding: 15px; /* 输入框大小放大 */
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
  width: 100%; /* 输入框宽度调整 */
}

.submit-button {
  background-color: #5cb85c;
  color: white;
  padding: 15px 30px; /* 按钮大小放大 */
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #4cae4c;
}

.result-screen h2 {
  font-size: 2em;
  margin-bottom: 0.5em;
}
.result-screen{
  font-size: 2em;
  margin-bottom: 0.5em;
}


.restart-button, .save-button {
  background-color: #337ab7;
  color: white;
  padding: 15px 30px; /* 按钮大小放大 */
  border: none;
  border-radius: 10px;
  cursor: pointer;
  margin-right: 10px; /* 按钮间距调整 */
  transition: background-color 0.3s ease;
}

.restart-button:hover, .save-button:hover {
  background-color: #3497da;
}

.play-screen .number {
  font-size: 3em; /* 增大数字大小 */
}

/* 输入界面样式 */
.input-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 30px; /* 与上方内容的间距 */
}

.submit-container {
  width: 100%; /* 按钮容器宽度 */
  text-align: center; /* 按钮水平居中 */
}
.level-up-screen {
  /* 升级界面的样式 */
  font-size: 2em;
  padding: 20px; /* 内边距 */
  border-radius: 10px; /* 边框圆角 */
  background-color: #3497da; /* 背景颜色 */
  color: white; /* 文字颜色 */
}

.level-up-screen h2 {
  font-size: 2.5em; /* 增大标题字体大小 */
  margin-bottom: 0.5em; /* 标题与内容的间距 */
}

.level-up-screen p {
  font-size: 1.5em; /* 增大段落字体大小 */
  margin-bottom: 1em; /* 段落与按钮的间距 */
}

.next-level-button {
  font-size: 1.2em; /* 按钮文字大小 */
  padding: 10px 20px; /* 按钮内边距 */
  border: none; /* 无边框 */
  border-radius: 5px; /* 按钮边框圆角 */
  background-color: #4CAF50; /* 按钮背景颜色 */
  color: white; /* 按钮文字颜色 */
  cursor: pointer; /* 鼠标悬停时显示手形图标 */
  transition: background-color 0.3s ease; /* 背景颜色变化的过渡效果 */
}

.next-level-button:hover {
  background-color: #45a049; /* 鼠标悬停时的按钮背景颜色 */
}
.timer-container {
  width: 100%;
  height: 20px;
  background-color: #ddd;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 10px;
}

.timer-bar {
  height: 100%;
  background-color: #87afc8;
  border-radius: 10px;
  transition: width 0.3s ease;
}
/* 其他样式可以根据需要添加 */
</style>
