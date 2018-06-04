import Vue from "vue";
import App from "./App.vue";
//导入router.js到入口文件
import router from './router';
//导入UI框架 全局引入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
//导入axios
import axios from 'axios'
//导入自定义图标
import './icon/iconfont.css'

// 注册全局函数
Vue.prototype.axios = axios;
//进行组件全局注册
Vue.use(ElementUI);

Vue.config.productionTip = false;

new Vue({
  router,
  // render: h => h(App)
  render:c =>c(App)
}).$mount("#app");