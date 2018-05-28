import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false


//element组件进行全局注册
Vue.use(ElementUI);


new Vue({
  // render: h => h(App)
  el: '#app',
  router,
  //render模板渲染函数
  render: c => c(App)
})
