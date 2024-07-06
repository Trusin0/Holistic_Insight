import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    userInfo: {
      id: '',
      username: ''
    },
    loading: false
  },
  mudules: {}
})

// 导出
export default store