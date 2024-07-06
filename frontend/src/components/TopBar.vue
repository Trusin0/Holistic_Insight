<template>
  <div id="top-bar-wrap">
    <div id="top-bar">
      <div class="top-bar-item">
        <span :class="{ active: $route.path === '/HelloWorld' }" @click="$router.push('/HelloWorld')">Holistic Insight</span>
        <span :class="{ active: $route.path === '/Tendency' }" @click="$router.push('/Tendency')">趋势</span>
      </div>
      <div v-if="$store.state.userInfo.username">
        <div class="top-bar-item">
          <span @click="logOut">退出登录</span>
        </div>
      </div>
      <div v-else>
        <div class="top-bar-item">
          <span :class="{ active: $route.path === '/Register' }" @click="$router.push('/Register')">注册</span>
          <span :class="{ active: $route.path === '/Login' }" @click="logIn">登录</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#top-bar-wrap {
  width: 100%;
  box-shadow: rgba(0, 0, 0, 0.2) 0px 0px 10px 0px;
  position: fixed;
  top: 0;
  left: 0;
  background-color: #fff;
  z-index: 100;
}
#top-bar {
  max-width: 1024px;
  height: 48px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 18px;
}
.top-bar-item {
  display: flex;
  height: 48px;
  align-items: center;
}
.top-bar-item span {
  display: block;
  line-height: 48px;
  padding: 0 10px;
  cursor: pointer;
}
.top-bar-item span.active {
  background-color: #e8eaed;
  pointer-events: none;
}
.top-bar-item span:hover {
  background-color: #e8eaed;
}
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
    logOut () {
      this.$message.success('已退出登录')
      for (let i in this.$store.state.userInfo) {
        this.$store.state.userInfo[i] = ''
      }
      window.localStorage.removeItem('human-benchmark-token')
      this.updateLoginStatus()
    },
    logIn () {
      this.$http.get('http://127.0.0.1:8000/api/auth/login')
        .then((response) => {
          window.open(response.data.redirect_url, '_blank')
          // window.location.href = response.data.redirect_url
        })
        .catch((error) => {
          console.error('Error during login:', error)
        })
    }
  }
}
</script>
