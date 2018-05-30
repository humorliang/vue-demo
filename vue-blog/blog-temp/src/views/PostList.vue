// 这是文章列表视图
<template>
    <div class="home">
        <el-container>
            <el-aside width="300px">
                <!-- 侧边组件 -->
                <aside-nav></aside-nav>
            </el-aside>
            <el-container>
                <el-main>
                    <!-- 列表头 -->
                    <post-list-title></post-list-title>
                    <!-- 二级视图挂载点 -->
                    <router-view :num="list"></router-view>
                    <!-- 分页 -->
                    <pagenation></pagenation>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
// @ is an alias to /src
import AsideNav from '@/components/AsideNav.vue'
import PostListTitle from '@/components/PostListTitle.vue'
import Pagenation from '@/components/Pagenation.vue'
export default {
    data(){
        return{
            list:['2','3','4','5']
        }
    },
    components: {
        "aside-nav": AsideNav,
        "post-list-title":PostListTitle,
        "pagenation":Pagenation
    }
};
</script>

<style scoped>
/* 演示 */
.home{
    margin: 10px;
}
.el-main{
    padding: 0 10px;
}
</style>
