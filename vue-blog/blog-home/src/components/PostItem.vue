<template>
    <div>
        <el-row v-for="item of data" :key="item.postId" class="post-item">
            <el-card class="box-card">
                <div class="post-tag pointer-click">
                    <el-tag
                    v-for="(la,index) of item.label"
                    :key='index'
                    type="success"
                    >{{la}}</el-tag>
                </div>
                <el-col :span="6">
                    <div class="grid-content">
                        <img :src="item.imgUrl" alt="文章图片"></div>
                </el-col>
                <el-col :span="17" class="post-content">
                    <div class="">
                        <h2 @click="toPostCon(item.postId)" class="pointer-click">{{item.title}}</h2>
                        <p class="pointer-click">
                            <!-- 对描述进行过滤 -->
                            {{strLength(item.description)}}
                        </p>
                        <div>
                            <div class="cf">
                                <div class="post-info">
                                    <div class=""><i class="iconfont icon-shijian"></i>{{item.time}}</div>
                                </div>
                                <div class="post-info">
                                    <div class="pointer-click" @click="toPostCon(item.postId)"><i class="iconfont icon-liulan"></i>({{item.viewNum}})</div>
                                </div>
                                <div class="post-info">
                                    <div class="pointer-click" @click="toPostCon(item.postId)"><i class="iconfont icon-pinglun"></i>({{item.commentNum}})</div>
                                </div>
                                <div class="post-info">
                                    <div class="pointer-click"><i class="iconfont icon-aixin"></i>({{item.thumbs}})</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </el-col>
            </el-card>
        </el-row>
    </div>
</template>


<script>
    /*  */
    export default {
        // 接受父组件的属性传参
        props: ["data"],
        methods:{
            toPostCon(id){
                // console.log(id);
                this.$router.push({name:'postCon',query:{id:id}})
            },
            strLength(str){
                //90字符
            if (str.length >= 90) {
                str = str.slice(0, 90) + '...'
                return str
            }else {
                return str
            }
            }
        },
        mounted: function() {
            
        }
    };
</script>


<style scoped>
.cf{
    overflow: hidden;
    padding-left: 20px;
}
.post-info{
    float: left;
    padding: 2px;
    margin: 0 5px;
}
    .pointer-click{
        cursor: pointer;
    }
    /*  */
    .post-tag {
        padding: 0 10px 10px 10px;
        cursor: pointer;
    }
    .post-tag .el-tag {
        margin: 0 10px;
    }
    .el-card {
        padding-bottom: 10px;
    }
    .post-item .el-col h2 {
        margin: 0;
        padding: 0 20px;
        font-size: 18px;
    }
    .post-item .el-col p {
        text-indent: 2em;
    }
    .post-item {
        margin: 20px 10px;
    }
    .post-item img {
        width: 100%;
    }
    .post-content {
        margin-left: 10px;
    }
    .post-content p{
        min-height: 70px;
    }
</style>
