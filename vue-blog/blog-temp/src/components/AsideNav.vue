<template>
    <div>
        <el-col :span="24">
            <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b"
            >
                <el-submenu index="1">
                    <template slot="title">
                        <i class="el-icon-date"></i>
                        <span>文章归档</span>
                    </template>
                    <el-menu-item-group>
                        <el-submenu index="1-1">
                            <template slot="title">2018年</template>
                            <el-menu-item index="1-1-1">2018(3)</el-menu-item>
                            <el-menu-item index="1-1-2">2018(2)</el-menu-item>
                        </el-submenu>
                        <el-submenu index="1-2">
                            <template slot="title">2017年</template>
                            <el-menu-item index="1-2-1">2017(3)</el-menu-item>
                            <el-menu-item index="1-2-2">2017(2)</el-menu-item>
                        </el-submenu>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index="2">
                    <template slot="title">
                        <i class="el-icon-menu"></i>
                        <span>文章分类</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="2-1">JavaScript</el-menu-item>
                        <el-menu-item index="2-2">python</el-menu-item>
                        <el-menu-item index="2-3">服务器</el-menu-item>
                        <el-menu-item index="2-4">vue</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index="3">
                    <template slot="title">
                        <i class="el-icon-tickets"></i>
                        <span>最新文章</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="3-1">文章一</el-menu-item>
                        <el-menu-item index="3-2">文章一</el-menu-item>
                        <el-menu-item index="3-3">文章一</el-menu-item>
                        <el-menu-item index="3-4">文章一</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index="4">
                    <template slot="title">
                        <i class="el-icon-loading"></i>
                        <span>随机推荐</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="4-1">文章一</el-menu-item>
                        <el-menu-item index="4-2">文章一</el-menu-item>
                        <el-menu-item index="4-3">文章一</el-menu-item>
                        <el-menu-item index="4-4">文章一</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>

                </el-menu>
        </el-col>
    </div>
</template>

<script>
export default {
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        }
    }
}
</script>

//
<style scoped>

</style>
