<template>
    <div id="app">
        <el-container>
            <el-header>
                <!-- 头部组件 -->
                <header-nav></header-nav>
            </el-header>
            <!-- 视图挂载点 -->
            <router-view/>
            <el-footer>
                <footer-bar></footer-bar>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
//导入组件
import HeaderNav from "./components/HeaderNav.vue";

import FooterBar from '@/components/FooterBar.vue'
export default {
    components: {
        "header-nav": HeaderNav,
        "footer-bar": FooterBar
    }
};
</script>

<style lang="stylus">
body {
    margin: 0;
}

.el-header {
    background: #545c64;
}

#app {
    min-width: 1200px;
}
</style>
