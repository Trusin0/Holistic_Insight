<template>
  <div id="top-bar">
    <button @click="goHome">Holistic Insight</button>
    <div v-if="isLoggedIn">
      <button @click="logout">Logout</button>
    </div>
    <div v-else>
      <button @click="login">Login</button>
    </div>
  </div>
</template>

<style scoped>
#top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f8f8f8;
}

button {
  padding: 8px 16px;
  font-size: 16px;
  cursor: pointer;
}

/* 可以根据需要添加更多样式 */
</style>

<script>
export default {
  name: 'TopBar',
  data () {
    return {
      msg: 'This is the TopBar component'
    }
  },
  methods: {
    goHome () {
      this.$router.push('/') // 跳转到首页
    },
    login () {
      this.isLoggedIn = true // 假设登录成功，更新状态为已登录
      // 这里可以添加实际的登录逻辑
    },
    logout () {
      this.isLoggedIn = false // 假设登出成功，更新状态为未登录
      // 这里可以添加实际的登出逻辑
    }
  }
}
</script>
