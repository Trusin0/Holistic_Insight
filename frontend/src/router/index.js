import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
//  routes: [
//    {
//      path: '*',
//      redirect: () => {
//        return '/index'
//      }
//    },
//    {
//      path: '/index',
//      component: () => import('@views/index')
//    }
//  ]
  routes: [
    {
      path: '/',
      // name: 'HelloWorld',
      name: 'HelloWorld',
      // component: HelloWorld
      component: HelloWorld
    }
  ]
})
