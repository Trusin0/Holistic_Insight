import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    userInfo: {
      id: '',
      username: '',
      token: '' || window.localStorage.getItem('holistic-insight-token')
    },
    loading: false
  },
  mudules: {}
})

// 导出
export default store
