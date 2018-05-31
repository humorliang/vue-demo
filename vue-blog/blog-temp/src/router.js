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
import NotFoundPage from './views/NotFoundPage.vue'
import MsgBoard from './views/MsgBoard.vue'
import HeaderNav from "./components/HeaderNav.vue";
import FooterBar from './components/FooterBar.vue'


export default new Router({
  routes: [{
      path: "/",
      name: "home",
      components: {
        "default": Home,
        "header": HeaderNav,
        "footer": FooterBar
      }
    },
    //文章列表路由
    {
      path: "/postList",
      redirect:{name:'menu',params:{kind:'js'}},
      components:{
        "default": PostList,
        "header": HeaderNav,
        "footer": FooterBar
      },
      //二级路由
      children: [
        //菜单栏路由
        {
          name: 'menu',
          path: 'menu/:kind',
          component: PostItem
        },
        //时间路由
        {
          name: 'dateKind',
          path: 'date/:time',
          component: PostItem
        },
        // 语言种类路由
        {
          name: 'languageKind',
            path: 'language/:name',
            component: PostItem
        }
      ]
    },
    {
      name: 'postCon',
      path: '/articleInfo/',
      components: {
        "default": PostCon,
        "header": HeaderNav,
        "footer": FooterBar
      }
    },
    {
      name: 'msgBoard',
      path: '/msgBoard',
      components: {
        "default": MsgBoard,
        "header": HeaderNav,
        "footer": FooterBar
      }
    },
    {
      path: '*',
      component: NotFoundPage
    }
  ],
  // 去除#号
  mode: 'history'
});