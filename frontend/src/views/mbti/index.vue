<template>
  <div>
    <!-- 开始界面 -->
    <div v-if="testStart === false" class="initial-screen">
      <p>MBTI性格测试</p>
      <button @click="start" class="button">开始测试</button>
    </div>
    <!-- 测试界面 -->
    <div v-else>
      <div v-if="testFinished === false" class="questionSet">
        <p class="questionSetText">{{ currentQuestionSet.text }}</p>
        <p class="questionText">{{ questionCounter }}. {{ currentQuestion.text }}</p>
        <p
          v-for="(option, index) in ['A', 'B']"
          :key="index"
          class="optionText"
          @click="selectOption(currentQuestion, option)"
        >
          <span class="hover-underline">{{option + '. ' + currentQuestion['option' + option + 'Text'] }}</span>
        </p>
      </div>
      <!-- 结果界面 -->
      <div v-else class="initial-screen">
        <p>测试完成</p>
        <p>你的性格类型是: {{ finalResult }}</p>
        <button @click="reset" class="button">重新测试</button>
      </div>
    </div>
  </div>
</template>

<script>
import jsonData from './questions.json'
export default {
  data () {
    return {
      testStart: false, // 测试是否开始
      questionSets: jsonData.questionSets,
      testFinished: false,
      questionCounter: 1, // 当前问题计数
      currentQuestionSetIndex: 0, // 当前题目集索引
      currentQuestionIndex: 0, // 当前题目索引
      currentQuestionSet: {}, // 当前题目集
      currentQuestion: {}, // 当前题目
      answerCount: {E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0}, // 回答统计
      finalResult: '' // 最终结果
    }
  },
  methods: {
    start () {
      // 初始化 当前题目集 与 当前题目
      this.currentQuestionSet = this.questionSets[this.currentQuestionSetIndex]
      this.currentQuestion = this.currentQuestionSet.questions[this.currentQuestionIndex]
      console.log(this.currentQuestion)
      console.log(this.currentQuestionSet)
      // 开始测试
      this.testStart = true
      console.log('测试开始')
    },
    selectOption (question, option) {
      console.log('点击选项')
      console.log(question)
      console.log(this.currentQuestionIndex)
      console.log(Object.keys(this.currentQuestionSet.questions).length)
      question.answer = option === 'A' ? question.optionAType : question.optionBType
      this.answerCount[question.answer]++ // 回答统计+1
      this.questionCounter++ // 当前问题计数+1
      this.currentQuestionIndex++ // 当前问题索引+1
      if (this.currentQuestionIndex === Object.keys(this.currentQuestionSet.questions).length) { // 完成单个题集
        this.currentQuestionSetIndex++ // 更新当前题集
        if (this.currentQuestionSetIndex === Object.keys(this.questionSets).length) { // 全部完成
          console.log('测试完成')
          console.log(this.answerCount)
          // 统计结果
          this.finalResult = (
            (this.answerCount.E > this.answerCount.I ? 'E' : 'I') +
            (this.answerCount.S > this.answerCount.N ? 'S' : 'N') +
            (this.answerCount.T > this.answerCount.F ? 'T' : 'F') +
            (this.answerCount.J > this.answerCount.P ? 'J' : 'P'))
          this.testFinished = true
        } else { // 还有题集
          this.currentQuestionSet = this.questionSets[this.currentQuestionSetIndex]
          this.currentQuestionIndex = 0 // 更新当前题目
          this.currentQuestion = this.currentQuestionSet.questions[this.currentQuestionIndex]
        }
      } else {
        this.currentQuestion = this.currentQuestionSet.questions[this.currentQuestionIndex]
      }
    },
    reset () {
      this.currentQuestionIndex = 0
      this.currentQuestionSetIndex = 0
      this.questionCounter = 1
      this.currentQuestionSet = this.questionSets[this.currentQuestionSetIndex]
      this.currentQuestion = this.currentQuestionSet.questions[this.currentQuestionIndex]
      this.answerCount = {E: 0, I: 0, S: 0, N: 0, T: 0, F: 0, J: 0, P: 0}
      this.finalResult = ''
      this.testFinished = false
      console.log(jsonData)
      console.log(jsonData.questionSets)
      console.log(jsonData.questionSets[0])
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
  background-color: #3496d9; /* 一个明亮的背景颜色 */
  text-align: center;
  padding: 20px; /* 添加一些内边距 */
  font-size: 70px; /* 增大字体大小，更易阅读 */
  color: #FFFFFFFC; /* 白色文字 */
  font-weight: bold; /* 字体加粗 */
}

/* 问题界面样式 */
.questionSet {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 100vh; /* 使初始屏幕填满视窗的高度 */
  background-color: #3496d9; /* 一个明亮的背景颜色 */
  color: #FFFFFFFC; /* 白色文字 */
  font-weight: bold; /* 字体加粗 */
}

/* 问题样式 */
.questionSetText {
  font-size: 28px;
  text-align: left;
  margin: 0 40px 0 ; /* 左右边距 */
}

/* 问题样式 */
.questionText {
  font-size: 23px;
  text-align: left;
  margin: 50px 100px 20px; /* 左右边距 */
}

/* 选项样式 */
.optionText {
  font-size: 23px;
  text-align: left;
  margin: 20px 130px 10px; /* 左右边距 */
  cursor: pointer;
  display: inline-block;
  position: relative;
  overflow: hidden;
  color: #ffffff;
  text-decoration: none;
  transition: color 0.3s;
}

.hover-underline {
  display: inline-block;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  color: #ffffff;
  text-decoration: none;
  transition: color 0.3s;
}
.hover-underline::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 50%;
  background-color: #FFFFFFFC;
  transition: width 0.3s ease, left 0.3s ease;
}
.hover-underline:hover::after {
  width: 100%;
  left: 0;
}

/* 按钮样式 */
.button {
  padding: 10px 20px; /* 按钮内边距 */
  font-size: 40px; /* 适中的按钮文本大小 */
  font-weight: bold; /* 字体加粗 */
  color: #FFFFFFFC; /* 白色文字 */
  background-color: rgba(98, 227, 142, 0.99); /* 按钮背景颜色 */
  border: none;
  border-radius: 10px; /* 圆角边框 */
  cursor: pointer; /* 显示手型光标表示可点击 */
}

</style>
