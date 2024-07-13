<template>
  <div class="charts">
    <div class="chart-container">
      <h1>Average Vs Me</h1>
      <!-- 图表显示 -->
      <img :src="average_url" alt="Average Plot" v-if="average_url">
    </div>
    <div class="chart-container">
      <h1>History Vs Me</h1>
      <!-- 图表显示 -->
      <img :src="history_url" alt="History Plot" v-if="history_url">
    </div>
  </div>
</template>


<script>
export default {
  props: {
    testName: {
      type: String,
      required: true
    },
    userId: {
      type: Number,
      default: 1 // 默认用户ID，实际应用中应该是动态获取
    }
  },
  computed: {
    average_url() {
      return `http://localhost:8000/api/plot/${this.testName}/${this.userId}/`;
    },
    history_url() {
      return `http://localhost:8000/api/plot/${this.testName}/${this.userId}/history/`;
    }
  }
}
</script>


<style scoped>
h1 {
  color: #2c3e50;
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
  letter-spacing: 2px;
}

.charts {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px; /* 这将为图表之间增加空隙 */
}

.chart-container {
  width: 80%;
  max-width: 800px;
}

img {
  width: 100%;
  height: auto;
  margin-top: 20px;
}
</style>
