<template>
    <div id="app">
        <el-container>
            <el-header>
                <!-- 头部组件 -->
                <!-- <header-nav></header-nav> -->
                <router-view name="header"></router-view>
            </el-header>
            <!-- 视图挂载点 -->
            <router-view/>
            <el-footer>
                <!-- <footer-bar></footer-bar> -->
                <router-view name="footer"></router-view>                
            </el-footer>
        </el-container>
    </div>
</template>

<script>
//导入组件
// import HeaderNav from "./components/HeaderNav.vue";
// import FooterBar from './components/FooterBar.vue'
// export default {
//     components: {
//         "header-nav": HeaderNav,
//         "footer-bar": FooterBar
//     }
// };
</script>

<style lang="stylus">
body {
    margin: 0;
}

header.el-header {
    padding:0;
}

#app {
    min-width: 1200px;
}
</style>
