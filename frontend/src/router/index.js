import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index'
Vue.use(VueRouter)

const routes = [

]

const router = new VueRouter({
  routes
})


router.beforeEach((to, from, next)=> {
})

export const defaultPage = '/';
export default router
