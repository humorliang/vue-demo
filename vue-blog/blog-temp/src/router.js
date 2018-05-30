import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import About from "./views/About.vue";

Vue.use(Router);


// 导入组件
import PostItem from './components/PostItem.vue'
import PostListTitle from './components/PostListTitle.vue'
import PostList from './views/PostList.vue'
import PostCon from './views/PostCon.vue'



export default new Router({
  routes: [{
      path: "/",
      name: "home",
      component: Home,
    },
    //文章列表路由
    {
      path: "/postList",
      component: PostList,
      //二级路由
      children: [{
        name:'VueJs',
        path: 'VueJs',
        component: PostItem
      }]
    },
    {
      path: "/about",
      name: "about",
      component: About
    },
    {
      name:'postCon',
      path:'/content',
      component:PostCon
    }
  ],
  // 去除#号
  mode: 'history'
});