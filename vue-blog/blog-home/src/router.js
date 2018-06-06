import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
//导入axios
import axios from 'axios'
// 注册全局函数
Vue.prototype.axios = axios;

Vue.use(Router);


// 导入组件
import PostList from './views/PostList.vue'
import Article from './views/Article.vue'
import NotFoundPage from './views/NotFoundPage.vue'
import Board from './views/Board.vue'



export default new Router({
  routes: [{
      path: "/",
      name: "home",
      component: Home
    },
    //文章列表路由
    {
      path: "/postList",
      name:"postlist",
      component: PostList
    },
    {
      path: '/article',
      name: 'article',
      component:Article
    },
    {
      path: '/board',
      name: 'board',
      component: Board
    },
    {
      path: '*',
      component: NotFoundPage
    }
  ],
  // 去除#号
  mode: 'history'
});