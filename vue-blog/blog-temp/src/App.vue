<template>
    <div id="app">
        <el-container>
            <el-header>
                <!-- 头部组件 -->
                <header-nav></header-nav>
            </el-header>
            <el-container>
                <el-aside width="200px">Aside</el-aside>
                <el-container>
                    <el-main>
                        <router-view/>
                    </el-main>
                    <el-footer>Footer</el-footer>
                </el-container>
            </el-container>
        </el-container>
    </div>
</template>

<script>
//导入组件
import HeaderNav from "./components/HeaderNav.vue";
export default {
    components: {
        "header-nav": HeaderNav
    }
};
</script>

<style lang="stylus">
body {
    margin: 0;
}
.el-header{
  background: #545c64;
}
#app {
    min-width: 1000px;
}
</style>
