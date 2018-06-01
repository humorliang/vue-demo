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
                        <el-menu-item
                            v-for="o in 3"
                            :key="o"
                            :index="'1-1-'+o"
                            @click="handlePostList"                            
                        >2018</el-menu-item>
                    </el-submenu>
                    <el-submenu index="1-2">
                        <template slot="title">2017年</template>
                        <el-menu-item
                            v-for="o in 3"
                            :key="o"
                            :index="'1-2-'+o"
                            @click="handlePostList"
                        >2017</el-menu-item>
                       </el-submenu>
                </el-menu-item-group>
            </el-submenu>
            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>文章分类</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item
                            v-for="o in 3"
                            :key="o"
                            :index="'2-'+o"
                            @click="handlePostList2"
                        >Python</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-submenu index="3">
                <template slot="title">
                    <i class="el-icon-tickets"></i>
                    <span>最新文章</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item
                            v-for="o in 3"
                            :key="o"
                            :index="'3-'+o"
                            @click="handlePostCon"
                        >文章一</el-menu-item>
                </el-menu-item-group>
            </el-submenu>
            <el-submenu index="4">
                <template slot="title">
                    <i class="el-icon-loading"></i>
                    <span>随机推荐</span>
                </template>
                <el-menu-item-group>
                    <el-menu-item
                            v-for="o in 3"
                            :key="o"
                            :index="'4-'+o"
                            @click="handlePostCon"
                        >文章1</el-menu-item>
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
        },
        handlePostList2(){
            this.$router.push({name:'languageKind',params:{name:'javascript'}})            
        },
        handlePostList(){
            this.$router.push({name:'dateKind',params:{time:'2018-2'}})
        },
        handlePostCon(){
            this.$router.push({name:'postCon',query:{id:'10201'}})
        }
    }
};
</script>


//
<style scoped>

</style>
