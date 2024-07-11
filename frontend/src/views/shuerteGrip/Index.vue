<template>
  <div>
    <!-- 初始界面 -->
    <div v-if="stage === 0" class="initial-screen">
      舒尔特测试
      <button @click="startGame">GO</button>
    </div>

    <!-- 游戏界面 -->
    <div v-if="stage === 1" class="game-screen">
      <div class="grid-container">
        <div v-for="(row, rowIndex) in grid" :key="rowIndex">
          <div
            v-for="(cell, cellIndex) in row"
            :key="cellIndex"
            :style="{ backgroundColor: cell.color }"
            :class="['grid-cell', { correct: cell.color === 'green', wrong: cell.color === 'gray' }]"
            @click="handleClick(cell, rowIndex, cellIndex)"
          >
            {{ cell.number }}
          </div>
        </div>
      </div>
    </div>

    <!-- 游戏结束界面 -->
    <div v-if="stage === 2" class="game-over-screen">
      你用时: {{ timeElapsed }}秒
      <button @click="resetGame">再来一次</button>
      <button @click="saveScore">保存成绩</button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    console.log('Game started') // 确认这个方法是否被调用
    return {
      size: 4, // 网格大小
      grid: [], // 网格
      stage: 0, // 当前阶段
      correctOrder: [], // 正确的顺序
      correctCount: 0, // 正确的数量
      timeStart: 0, // 游戏开始时间
      timeElapsed: 0 // 游戏用时
    }
  },
  methods: {
    startGame () {
      console.log('Game started') // 确认这个方法是否被调用

      // 生成从1到size^2的数字数组
      const totalCells = this.size * this.size
      const numbers = Array.from({length: totalCells}, (_, index) => index + 1)

      // 打乱数组（Fisher-Yates洗牌算法）
      for (let i = numbers.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1)) // 生成0到i的随机数
        const temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp
      }

      // 填充 correctOrder，每个数字的值指向其索引
      this.correctOrder = new Array(numbers.length)
      numbers.forEach((number, index) => {
        this.correctOrder[number - 1] = index
      })

      // 填充网格
      this.grid = []
      for (let i = 0; i < this.size; i++) {
        const start = i * this.size
        const end = start + this.size
        const row = numbers.slice(start, end).map(number => ({ // 对象类型转换
          number: number,
          color: 'lightgrey' // 初始化颜色
        }))
        this.grid.push(row)
      }

      this.correctCount = 0
      this.timeStart = 0
      this.timeElapsed = 0
      this.stage = 1
      console.log('Game started, gameStarted:', this.gameStarted) // 检查 gameStarted 状态
    },
    handleClick (cell, rowIndex, cellIndex) {
      const currentIndex = rowIndex * this.size + cellIndex

      // 初次点击才开始计时
      if (this.timeStart === 0 && this.correctCount === 0) {
        this.timeStart = Date.now()
      }

      if (this.correctOrder[this.correctCount] === currentIndex) {
        cell.color = 'green' // 将cell颜色置为绿色
        this.correctCount++ // 增加正确点击的计数

        // 完成所有点击，游戏结束
        if (this.correctCount === this.correctOrder.length) {
          this.timeElapsed = (Date.now() - this.timeStart) / 1000
          this.stage = 2
        }
      } else if (cell.number > this.correctCount + 1) {
        cell.color = 'gray' // 将cell颜色置为灰色
      }
    },
    resetGame () {
      this.stage = 0
    },
    saveScore () {
      const currentTime = new Date().getTime() // 记录当前时间
      this.$http.get('http://127.0.0.1:8000/api/game/save_game_data?game_name=schulte&error_times=0&block_size=4&cost=' + (this.timeElapsed) + '&usr_name=' + this.$store.state.userInfo.username + '&play_time=' + currentTime)
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
  background-color: #3495d8; /* 一个明亮的背景颜色 */
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
  background-color: rgba(98, 227, 142, 0.99); /* 按钮背景颜色 */
  border: none;
  border-radius: 10px; /* 圆角边框 */
  cursor: pointer; /* 显示手型光标表示可点击 */
  transition: background-color 0.2s; /* 过渡效果让按钮的变化更平滑 */
}

.initial-screen button:hover {
  background-color: #02a33f; /* 鼠标悬停时按钮颜色加深 */
}

/* 游戏界面样式 */
.game-screen {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh; /* 使初始屏幕填满视窗的高度 */
  background-color: #3496d9; /* 一个明亮的背景颜色 */
  color: #333333; /* 文本颜色 */
  text-align: center;
  padding: 20px; /* 添加一些内边距 */
}

/* 网格容器样式 */
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 根据网格的列数调整 */
  grid-template-rows: repeat(4, 1fr); /* 创建4行，确保是4x4的网格 */
//column-gap: 5px; /* 网格之间的间隙 */ //row-gap: 10px; /* 网格之间的间隙 */ padding: 10px; /* 容器的内边距 */
  margin: auto; /* 居中显示 */
  width: 100%; /* 容器宽度，根据实际需要调整 */
  height: 100%; /* 容器长度，根据实际需要调整 */
  max-width: 540px; /* 最大宽度限制 */
  max-height: 540px; /* 最大长度限制 */
  aspect-ratio: 1 / 1; /* 保持容器为正方形 */
  background: #e0e0e0; /* 轻灰色背景，可以根据主题调整 */
  border-radius: 30px; /* 圆角边框 */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* 轻微的阴影效果提升层次感 */
}

/* 单元格样式 */
.grid-cell {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #9d9d9d; /* 轻灰色背景，可以根据主题调整 */
  width: 100%; /* 充满容器列宽 */
  height: 70%; /* 充满容器行高 */
  font-size: 36px; /* 数字的字体大小 */
  font-weight: bold; /* 字体加粗 */
  color: #333; /* 字体颜色，提高可读性 */
  cursor: pointer; /* 表明这是一个可点击的元素 */
//aspect-ratio: 1 / 1; /* 保持单元格为正方形 */ border-radius: 25px; /* 圆角边框 */
  transition: background-color 0.3s, transform 0.2s; /* 平滑的背景色变化和轻微放大效果 */
}

/* 当单元格正确时的样式 */
.correct {
  background-color: #4CAF50; /* 正确的绿色 */
  color: #ffffff; /* 白色字体增强对比 */
}

/* 当单元格错误时的样式 */
.wrong {
  background-color: #595959; /* 错误的灰色 */
  color: #ffffff; /* 白色字体增强对比 */
}

/* 单元格点击效果 */
.grid-cell:active {
  transform: scale(0.9); /* 点击时轻微缩小，增加交互感 */
}

.game-over-screen {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh; /* 使初始屏幕填满视窗的高度 */
  background-color: #3496d9; /* 一个明亮的背景颜色 */
  text-align: center;
  padding: 20px; /* 添加一些内边距 */
  font-size: 50px; /* 增大字体大小，更易阅读 */
  color: #FFFFFFFC; /* 白色文字 */
  margin-bottom: 80px; /* 添加下边距 */
  font-weight: bold; /* 字体加粗 */
}

.game-over-screen button {
  padding: 10px 20px; /* 按钮内边距 */
  font-size: 40px; /* 适中的按钮文本大小 */
  font-weight: bold; /* 字体加粗 */
  color: #FFFFFFFC; /* 白色文字 */
  background-color: rgba(98, 227, 142, 0.99); /* 按钮背景颜色 */
  border: none;
  border-radius: 10px; /* 圆角边框 */
  cursor: pointer; /* 显示手型光标表示可点击 */
  transition: background-color 0.2s; /* 过渡效果让按钮的变化更平滑 */
}

.game-over-screen button:hover {
  background-color: #02a33f; /* 鼠标悬停时按钮颜色加深 */
}

.button:hover {
  background-color: #0056b3; /* 鼠标悬停时的背景颜色 */
}

@media (max-width: 600px) {
  .grid-container {
    width: 90%; /* 在小屏设备上更宽 */
    max-width: 300px; /* 最大宽度更小 */
  }

  .grid-cell {
    height: 60px; /* 单元格在小屏幕上更小 */
  }

  .button {
    font-size: 14px; /* 按钮文字大小适应小屏幕 */
  }
}

</style>

// WEBPACK FOOTER //
// src/views/shuerteGrip/Index.vue
