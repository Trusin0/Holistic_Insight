<template>
  <div>
    <h1>Test Details for {{ testName }}</h1>
    <!-- 图表显示 -->
    <img :src="imageUrl" alt="Test Plot" v-if="imageUrl">
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
    imageUrl() {
      return `http://localhost:8000/plot/${this.testName}/${this.userId}/`;
    }
  }
}
</script>


<style scoped>
h1 {
  color: #333;
  margin-bottom: 20px;
}
img {
  width: 100%; 
  height: auto;
}
</style>
