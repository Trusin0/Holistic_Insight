<template>
  <tr>
    <td class="test-name">{{ test.name }}</td>
    <td class="actions">
      <a @click="playTest(test.name)" class="action-link">Play</a> |
      <a @click="viewStats(test.name)" class="action-link">Stats</a>
    </td>
    <td class="score">{{ test.score !== null ? test.score + ' points' : '?' }}</td>
    <td class="percentile">
      <div class="percent-bar" v-if="test.percentile !== null" :style="{ width: test.percentile + '%' }"></div>
      <span>{{ test.percentile !== null ? test.percentile + '%' : '?' }}</span>
    </td>
  </tr>
</template>

<script>
export default {
  props: {
    test: Object
  },
  methods: {
    playTest(testName) {
      window.location.href = `/#/${testName}`;
    },
    viewStats(testName) {
      // 使用vue-router进行页面跳转
      this.$router.push({ name: 'data', params: { testName } });
    }
  }
}
</script>


<style scoped>
.test-name {
  font-weight: bold;
}

.actions {
  color: blue;
}

.action-link {
  color: #3498db;
  cursor: pointer;
  text-decoration: none;
}

.action-link:hover {
  text-decoration: underline;
}

.score {
  text-align: center;
}

.percentile {
  position: relative;
  text-align: center;
}

.percent-bar {
  position: absolute;
  left: 0;
  top: 50%;
  height: 10px;
  background-color: #3498db;
  z-index: 0;
}

.percentile span {
  position: relative;
  z-index: 1;
  padding: 0 5px;
  background: white;
}
</style>
