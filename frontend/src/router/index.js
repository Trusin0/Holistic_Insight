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
    },
    {
      path: '/shuerte-grip',
      component: () => import(`@/views/shuerteGrip/Index.vue`)
    },
    {
      path: '/aim-test',
      component: () => import(`@/views/aimTest/Index.vue`)
    },
    {
      path: '/mbti',
      component: () => import(`@/views/mbti/Index.vue`)
    },
    {
      path: '/number-memory',
      component: () => import(`@/views/numberMemory/Index.vue`)
    },
    {
      path: '/figure-memory',
      component: () => import(`@/views/figureMemory/Index.vue`)
    },
    {
      path: '/color-sensitivity',
      component: () => import(`@/views/colorSensitivity/Index.vue`)
    },
    {
      path: '/Dashboard',
      component: () => import(`@/views/Dashboard/Index.vue`)
    }
  ]
})
