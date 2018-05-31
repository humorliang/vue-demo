/* 这是主页视图 */
<template>
    <div class="home">
        <el-container>
            <el-aside width="300px">
                <!-- 侧边组件 -->
                <aside-nav></aside-nav>
            </el-aside>
            <el-container>
                <el-main>
                    <!-- 二级视图挂载点 -->
                    <div class="block">
                        <el-carousel height="350px">
                            <el-carousel-item
                                v-for="item in 4"
                                :key="item"
                            >
                                <h3>{{ item }}</h3>
                                </el-carousel-item>
                        </el-carousel>
                    </div>
                    <!-- 主页文章 -->
                    <post-item :num='list'></post-item>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
// @ is an alias to /src
import AsideNav from '@/components/AsideNav.vue'
import PostItem from '@/components/PostItem.vue'

export default {
    data() {
        return {
            list:['1', '2', '3']
        }
    },
    components: {
        "aside-nav": AsideNav,
        "post-item":PostItem
    }
};
</script>

<style scoped>
/* 演示 */
.el-main{
    padding: 0 10px;
}
.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 350px;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
}
.home{
    padding: 10px;
}
</style>
