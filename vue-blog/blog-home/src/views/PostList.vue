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
                    <router-view :data="data"></router-view>
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
            data:[]
        }
    },
    created:function(){
        // 文章数据
        var postdata=[
            {postId:'1',imgUrl:'http://a.hiphotos.baidu.com/image/pic/item/730e0cf3d7ca7bcb6a172486b2096b63f624a82f.jpg',title:'文章的标题',description:'这是一段文章的简介',author:'tempt',time:'2017-2-6',viewNum:'100',commentNum:'7',thumbs:'10',label:['label1','label2']},
            {postId:'2',imgUrl:'http://a.hiphotos.baidu.com/image/pic/item/730e0cf3d7ca7bcb6a172486b2096b63f624a82f.jpg',title:'文章的标题2',description:'这是一段文章的简介',author:'tempt',time:'2017-6-3',viewNum:'100',commentNum:'6',thumbs:'11',label:['label1','label2']},
            {postId:'3',imgUrl:'http://a.hiphotos.baidu.com/image/pic/item/730e0cf3d7ca7bcb6a172486b2096b63f624a82f.jpg',title:'文章的标题3',description:'这是一段文章的简介',author:'tempt',time:'2017-5-6',viewNum:'100',commentNum:'5',thumbs:'12',label:['label1','label2']},
        ];
        this.data=postdata; 
        console.log(this.data);
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
