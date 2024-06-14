import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/views/index/Index.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '*',
      redirect: () => {
        return '/Index'
      }
    },
    {
      path: '/Index',
      component: Index
    },
    {
      path: '/reaction-time',
      component: () => import(`@/views/reactionTime/Index.vue`)
    }
  ]
})
