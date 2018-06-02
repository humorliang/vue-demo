import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";

import main from './views/main.vue';
import post from './views/post/post.vue'
import user from './views/user/user.vue'
import comment from './views/comment/comment.vue'
import leaveMsg from './views/comment/leaveMsg.vue'
import postclass from './views/postclass/postclass.vue'
import addarticle from './views/post/addaticle.vue'

Vue.use(Router);

export default new Router({
  routes: [{
    path: "/",
    name: "home",
    redirect: {
      name: 'main'
    },
    component: Home,
    children: [{
      path: "main",
      name: "main",
      component: main
    }, {
      path: "post",
      name: "post",
      component: post
    }, {
      path: "addarticle",
      name: "addarticle",
      component: addarticle
    }, {
      path: "user",
      name: "user",
      component: user
    }, {
      path: "comment",
      name: "comment",
      component: comment
    }, {
      path: "leaveMsg",
      name: "leaveMsg",
      component: leaveMsg
    }, {
      path: "kind",
      name: "kind",
      component: postclass
    }]
  }, {
    path: "/login",
    name: "login",
    component: Login
  }],
  mode:'history'
});