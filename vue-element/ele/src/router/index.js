import Vue from 'vue'
import Router from 'vue-router'

//挂载到根实例上
Vue.use(Router)

//导入组件
import Main from '../components/Main.vue'


export default new Router({
    // 路由注册
    routes: [{
        path:'/',
        component:Main
    }]
})