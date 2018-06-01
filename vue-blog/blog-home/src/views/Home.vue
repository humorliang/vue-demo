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
                    <post-item :data="data"></post-item>
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
            data:''
        }
    },
    created:function(){
        // 文章数据
        var postdata=[
            {postId:'1',imgUrl:'http://a.hiphotos.baidu.com/image/pic/item/730e0cf3d7ca7bcb6a172486b2096b63f624a82f.jpg',title:'文章的标题111',description:'这是一段文章的简介',author:'tempt',time:'2017-2-6',viewNum:'100',commentNum:'7',thumbs:'10',label:['label1','label2']},
            {postId:'2',imgUrl:'http://a.hiphotos.baidu.com/image/pic/item/730e0cf3d7ca7bcb6a172486b2096b63f624a82f.jpg',title:'文章的标题211',description:'这是一段文章的简介',author:'tempt',time:'2017-6-3',viewNum:'100',commentNum:'6',thumbs:'11',label:['label1','label2']},
            {postId:'3',imgUrl:'http://a.hiphotos.baidu.com/image/pic/item/730e0cf3d7ca7bcb6a172486b2096b63f624a82f.jpg',title:'文章的标题311',description:'这是一段文章的简介',author:'tempt',time:'2017-5-6',viewNum:'100',commentNum:'5',thumbs:'12',label:['label1','label2']},
        ];
        this.data=postdata; 
        // console.log(this.data);
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
