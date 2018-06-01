import Vue from "vue";
import App from "./App.vue";
//导入router.js到入口文件
import router from './router';
//导入UI框架 全局引入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

//导入自定义图标
import './icon/iconfont.css'

//进行组件全局注册
Vue.use(ElementUI);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
