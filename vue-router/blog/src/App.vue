<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- 给路由进行留坑 -->
    <header-nav></header-nav>
    <!-- <router-view name="header"/>
    <router-view />
    <router-view name="footer"/> -->
    <router-view/>
    <footer-nav></footer-nav>
  </div>
</template>

<script>
import HeaderNav from './components/HeaderNav'
import FooterNav from './components/FooterNav'
export default {
  name: 'App',
  components:{
    'header-nav':HeaderNav,
    'footer-nav':FooterNav
  }
}
</script>

<style>

</style>
