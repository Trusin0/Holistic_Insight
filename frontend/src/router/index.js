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
      name: 'index',
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
      path: '/oauth/callback',
      name: 'oauthCallback',
      component: () => import('@/components/OAuthCallback.vue')
    },
    {
      path: '/aim-test',
      component: () => import(`@/views/aimTest/Index.vue`)
    }
  ]
})
