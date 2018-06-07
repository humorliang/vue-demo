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
import AllPostList from './views/AllPostList.vue'
import Article from './views/Article.vue'
import NotFoundPage from './views/NotFoundPage.vue'
import Board from './views/Board.vue'
import Base from './views/Base.vue'



export default new Router({
  routes: [{
      path: "/",
      name: "base",
      component: Base,
      redirect: {
        name: 'home'
      },
      children: [{
          path: "home",
          name: "home",
          component: Home
        },
        //文章列表路由
        {
          path: "postlist/:kind_id/",
          name: "postlist",
          component: PostList
        },
        {
          path: "menupost/:t/",
          name: "menupost",
          component: AllPostList
        },
        {
          path: 'article/:id/',
          name: 'article',
          component: Article
        },
        {
          path: 'board',
          name: 'board',
          component: Board
        },
      ]
    },
    {
      path: '*',
      component: NotFoundPage
    }
  ]
});