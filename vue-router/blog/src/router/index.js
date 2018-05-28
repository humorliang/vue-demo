import Vue from 'vue'
import Router from 'vue-router'



//导入组件
import HeaderNav from '@/components/HeaderNav'
import FooterNav from '@/components/FooterNav'
import MainContent from '@/components/MainContent'
import MusicNav from '@/components/MusicNav'
import VideoNav from '@/components/VideoNav'
import MusicMain from '@/components/MusicMain'
import VideoMain from '@/components/VideoMain'
import ChinaMusic from '@/components/ChinaMusic'
import EnglishMusic from '@/components/EnglishMusic'


// 声明vue-router插件
Vue.use(Router)
//路由注册
export default new Router({
  // 路由路径
  routes: [
    //多视图路由
    // {
    //   path: '/',
    //   components: {
    //     //使用坑名应用组件
    //     header:HeaderNav,
    //     default:MainContent,
    //     footer:FooterNav
    //   }
    // }
    // 路由嵌套
    {
      path: '/',
      component: MainContent
    },
    {
      name: 'music',
      path: '/music',
      component: MusicNav,
      //定义子路由
      children: [{
          name: 'music_china',
          //路由传参
          path: 'china',
          component: ChinaMusic
        },
        {
          name: 'music_english',
          path: 'english',
          component: EnglishMusic
        }
      ]
    }
  ]
})
