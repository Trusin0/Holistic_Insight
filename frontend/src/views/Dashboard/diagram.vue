<template>
  <div>
    <h1>Test Details for {{ testName }}</h1>
    <img :src="plotUrl" alt="Test Plot">
  </div>
</template>

<script>
export default {
  props: {
    testName: {
      type: String,
      required: true
    }
  },
  computed: {
    plotUrl() {
      // 假设 Django 服务器运行在 localhost:8000
      // 需要确保 testName 是一个有效的测试类型
      return `http://127.0.0.1:8000/plot/${this.testName}/${this.userId}/`;
    }
  },
  data() {
    return {
      // 假设用户ID是已知的，或者可以通过某种方式获得
      userId: 1
    };
  },
  mounted() {
    console.log('Fetching plot for test:', this.testName);
  }
}
</script>

<style scoped>
h1 {
  color: #333;
  margin-bottom: 20px;
}
</style>
