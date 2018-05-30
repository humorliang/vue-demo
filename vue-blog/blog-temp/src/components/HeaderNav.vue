<template>
    <div>
        <el-menu
            :default-active="activeIndex"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
        >
            <div class="header-logo">
                <img
                    src="../assets/img/logo.png"
                    alt="龙在江湖"
                    class="logo"
                ></div>
            <el-menu-item index="1">首页</el-menu-item>
            <el-submenu index="2">
                <template slot="title">前端厨房</template>
                <el-menu-item index="2-1">Vue小菜</el-menu-item>
                <el-menu-item index="2-2">布局谋篇</el-menu-item>
                <el-menu-item index="2-3">JS利器</el-menu-item>
            </el-submenu>
            <el-submenu index="3">
                <template slot="title">后端囧事</template>
                <el-menu-item index="3-1">服务器</el-menu-item>
                <el-menu-item index="3-2">Python</el-menu-item>
                <el-menu-item index="3-3">数据库</el-menu-item>
            </el-submenu>
            <el-menu-item index="4">
                数据爬虫
            </el-menu-item>
            <el-menu-item index="5">
                来撩我
            </el-menu-item>
            <el-menu-item index="6" class="login">
                <router-link to="">登录</router-link>
            </el-menu-item>
            </el-menu>
    </div>
</template>


<script>
export default {
    data() {
        return {
            activeIndex: "1"
        };
    },
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        }
    }
};
</script>


<style scoped>
.header-logo {
    float: left;
    height: 60px;
    margin-right: 100px;
    line-height: 60px;
}
.logo {
    height: 80%;
    vertical-align: middle;
}
li.el-menu-item.login{
    float: right;
    margin-right: 20px;
}
li.el-menu-item.login a{
    text-decoration: none;
}
</style>
