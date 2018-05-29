import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';


//进行组件注册
Vue.use(ElementUI);


Vue.config.productionTip = false;

new Vue({
  router,
  //模板渲染函数
  render: h => h(App)
  //进行组件挂载
}).$mount("#app");
