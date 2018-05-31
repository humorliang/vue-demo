// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
//对根组件进行导入
import TodoList from './TodoList'

import VueDisqus from 'vue-disqus'

Vue.use(VueDisqus)


Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#root',
  components: { TodoList },
  template: '<TodoList/>'
})
