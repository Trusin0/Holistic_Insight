<template>
  <div class="container">
    <div id="app" class="game-container">
      <!-- 游戏开始界面 -->
      <div v-show="gameState === 'start'" class="start-screen">
        <h1>方块图像记忆测试-黑猩猩测试</h1>
        <p>根据方块的编号，依次单击方块，测试会越来越难</p>
        <button @click="startGame" class="start-button">开始</button>
      </div>

      <!-- 游戏进行界面 -->
      <div v-show="gameState === 'play'" class="play-screen">
        <div class="grid-container">
          <!-- 动态生成的网格 -->
          <div
            v-for="(cell, index) in grid"
            :key="index"
            class="grid-item"
            :class="{ 'memory-block-num': cell.NoTouch && cell.memoryBlock && cell.number > 0 , 'memory-block': cell.memoryBlock, 'has-number': cell.number > 0, 'incorrect': cell.incorrect, 'default':true }"
            @click="selectSquare(index)"
          >
            <!-- 仅当 cell.number 不是 -1 且 cell 不在记忆状态时显示数字 -->
            <span v-if="cell.number > 0 && (!cell.memoryBlock || cell.incorrect) ">{{ cell.number }}</span>
          </div>
        </div>
        <p v-if="allMemoryBlocksFalse" class="instruction-message">点击任意处后才正式开始噢~</p>
        <div v-if="levelComplete" class="level-complete">
          <p>Level {{ level }}</p>
          <button @click="nextLevel" class="next-level-button">NEXT</button>
        </div>
      </div>
      <!-- 游戏结束界面 -->
      <div v-show= "gameState === 'end'" class="game-over-screen">
        <h2>游戏结束</h2>
        <p>您已通关到 Level {{ level }}</p>
        <button @click="restartGame" class="restart-button">重新开始</button>
        <button @click="saveScore" class="save-score-button">保存成绩</button>
      </div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  data() {
    return {
      gameState: 'start',
      level: 1,
      grid: [],
      selectedNumbers: [],
      numberCount: 2, // 开始时n=2
      levelComplete: false,
    };
  },
  computed: {
    allMemoryBlocksFalse() {
      return !this.grid.some(cell => cell.memoryBlock);
    },
  },
  methods: {
    restartGame(){
      this.level = 1;
      this.numberCount = 2;
      this.initGrid();
      this.selectedNumbers = [];
      this.levelComplete = false;
      this.initGrid();
      this.gameState = 'play';
    },
    startGame() {
      this.initGrid();
      this.gameState = 'play';
    },
    initGrid() {
      this.grid = Array.from({ length: 60 }, () => ({ number: -1, incorrect: false, memoryBlock: false, NoTouch:true, }));
      this.fillNumbers();
    },
    fillNumbers() {
      const numbers = Array.from({ length: this.numberCount }, (_, i) => i + 1);
      const usedIndices = new Set(); // 创建一个集合来存储已经使用的索引

      numbers.forEach(number => {
        let index;
        do {
          index = Math.floor(Math.random() * 60); // 生成随机索引
        } while (usedIndices.has(index)); // 检查索引是否已使用

        usedIndices.add(index); // 将新索引添加到集合中

        // 更新grid数组，确保索引未被使用
        this.grid[index] = { ...this.grid[index], number };
      });
    },
    selectSquare(index) {
      let cell;
      cell = this.grid[index];
      if (cell.incorrect || this.levelComplete || !cell.number>0) return;

      // 如果是首次点击，并且点击的格子有数字，则开始记忆状态
      if (this.selectedNumbers.length === 0) {
        this.grid.forEach(cell => {
          cell.memoryBlock = true;
        });
        this.selectedNumbers.push(0);
      } else {
        if (cell.incorrect) {
          setTimeout(() => this.gameOver(), 10);
        } else {
          this.selectedNumbers.push(cell.number);
          Vue.set(cell, 'NoTouch', false);
          this.grid[index].incorrect = !this.checkSequence();
          if (this.grid[index].incorrect) {
            this.grid.forEach(cell => {
              if (cell.number > 0) {
                cell.incorrect = true;
              }
            });
            setTimeout(() => this.gameOver(), 1500);
          }
          if (this.selectedNumbers.length === this.numberCount+1) {
            this.levelComplete = true;
          }
        }
      }
      this.$forceUpdate()
    },
    checkSequence() {
      // 检查当前选择的数字是否按顺序递增
      for (let i = 1; i < this.selectedNumbers.length; i++) {
        // 比较当前数字与前一个数字加1是否相等
        if (this.selectedNumbers[i] !== this.selectedNumbers[i - 1] + 1) {
          // 如果任何数字不满足递增条件，返回false
          return false;
        }
      }
      // 如果所有数字都满足递增条件，返回true
      return true;
    },
    nextLevel() {
      if (!this.levelComplete) return;
      this.level++;
      this.numberCount++;
      this.initGrid();
      this.levelComplete = false;
      this.selectedNumbers = [];
      this.grid.forEach(cell => (cell.memoryBlock = false));
      this.gameState = 'play';
    },
    gameOver() {
      // 显示游戏结束界面
      this.gameState = 'end';
    },
    saveScore () {
      const currentTime = new Date().getTime() // 记录当前时间
      this.$http.get('http://127.0.0.1:8000/api/game/save_game_data?game_name=figureMemory&level=' + (this.level) + '&usr_name=' + this.$store.state.userInfo.username + '&play_time=' + currentTime)
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
.container {
  background-color: #3497da; /* 背景颜色 */
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100vw; /* 视口宽度的100% */
  height: 100vh; /* 视口高度的100% */
  margin: 0;
  padding: 0;
}
.game-container {
  background-color: #3497da; /* 背景颜色 */
  color: white; /* 文字颜色 */
  font-family: 'Arial', sans-serif; /* 字体 */
  text-align: center; /* 文本居中 */
  margin: 0 auto; /* 外边距自动，水平居中 */
  padding: 2rem; /* 内边距 */
  max-width: 60%; /* 最大宽度 */
  border-radius: 10px; /* 边框圆角 */
}

.start-screen h1 {
  color: white;
  font-size: 3em; /* 增大标题字体大小 */
  margin-bottom: 0.5em; /* 标题下边距 */
}

.start-button {
  background-color: #4CAF50; /* 按钮背景色 */
  color: white; /* 按钮文字颜色 */
  padding: 10px 20px; /* 按钮内边距 */
  border: none; /* 无边框 */
  border-radius: 5px; /* 按钮圆角 */
  cursor: pointer; /* 鼠标悬停时显示手形图标 */
  font-size: 2em; /* 按钮文字大小 */
  transition: background-color 0.3s ease, box-shadow 0.3s ease; /* 背景色和内阴影变化过渡 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* 添加内阴影 */
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3); /* 添加文字阴影 */
}

.start-button:hover {
  background-color: #45a049; /* 鼠标悬停时按钮背景色 */
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3); /* 悬停时内阴影加深 */
}

.play-screen {
  margin-top: 20px; /* 游戏进行界面上边距 */
  padding: 1rem; /* 增加内边距 */
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(10, 1fr); /* 10列的网格布局 */
  gap: 0.5rem; /* 调整网格间隙 */
  margin-bottom: 20px; /* 网格下边距 */
}

.grid-item {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #3497da; /* 格子背景色 */
  border: 1px solid #3497da; /* 边框 */
  border-radius: 5px; /* 边框圆角 */
  width: 80px; /* 增大网格项宽度 */
  height: 80px; /* 增大网格项高度 */
  font-size: 3em; /* 增大数字字体大小 */
  cursor: pointer; /* 鼠标悬停时显示手形图标 */
  transition: transform 0.2s, background-color 0.3s; /* 为网格项添加变换和背景色过渡 */
}

.grid-item:hover {
  transform: scale(1.05); /* 鼠标悬停时放大网格项 */
}
.grid-item.default {
  /* 有数字的格子样式 */
  background-color: #3497da; /* 显示状态为浅蓝色 */
}
.grid-item.has-number {
  /* 有数字的格子样式 */
  background-color: rgba(98, 227, 142, 0.99); /* 显示状态为浅蓝色 */
}

.grid-item.memory-block {
  /* 记忆状态的纯色块 */
  background-color: #3497da; /* 纯色块颜色 */
}

.grid-item.memory-block-num {
  /* 记忆状态的数字纯色块 */
  background-color: #ffffff; /* 纯色块颜色 */
}

.grid-item.incorrect {
  /* 错误状态的格子样式 */
  background-color: #d61124; /* 错误时的背景色 */
}

.level-complete {
  text-align: center; /* 等级完成文本居中 */
  font-size: 3em;
  margin-top: 2rem; /* 增大上边距 */
}

.next-level-button {
  padding: 10px 20px; /* 下一关按钮内边距 */
  font-size: 1em; /* 下一关按钮文字大小 */
  background-color: #4CAF50; /* 下一关按钮背景色 */
  color: white; /* 下一关按钮文字颜色 */
  border: none; /* 无边框 */
  border-radius: 5px; /* 圆角 */
  cursor: pointer; /* 鼠标悬停时显示手形图标 */
  transition: background-color 0.3s ease, box-shadow 0.3s ease; /* 背景色和内阴影变化过渡 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* 添加内阴影 */
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3); /* 添加文字阴影 */
}

.next-level-button:hover {
  background-color: #45a049; /* 鼠标悬停时按钮背景色 */
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3); /* 悬停时内阴影加深 */
}
.game-over-screen {
  font-size: 2em;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-top: 2rem;
  gap: 5px;
}

/* 可以添加一些动画或过渡效果使界面更友好 */
.game-over-screen h2 {
  margin-bottom: 1rem;
}

.restart-button,
.save-score-button {
  padding: 10px 20px;
  margin: 0 10px;
  font-size: 1em;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.restart-button {
  background-color: #4CAF50;
  color: white;
}

.restart-button:hover {
  background-color: #45a049;
}

.save-score-button {
  background-color: #f0ad4e;
  color: white;
}

.save-score-button:hover {
  background-color: #ec971f;
}
.instruction-message {
  font-size: 2em; /* 增大字号 */
  color: white; /* 确保文字颜色与背景对比明显 */
  margin-top: 1em; /* 与网格的间距 */
  /* 如果需要，还可以添加其他样式 */
}
</style>
