import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Blockchain from '@/components/Blockchain'
import Mine from '@/components/Mine'
import Transaction from '@/components/Transaction'
import User from '@/components/User'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/blockchain',
      name: 'blockchain',
      component: Blockchain
    },
    {
      path: '/transaction',
      name: 'transaction',
      component: Transaction
    },
    {
      path: '/user',
      name: 'user',
      component: User
    },
    {
      path: '/mine',
      name: 'mine',
      component: Mine
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})
