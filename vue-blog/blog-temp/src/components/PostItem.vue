<template>
    <div>
        <el-row v-for="item of num" :key="item" class="post-item">
            <el-card class="box-card">
                <div class="post-tag">
                    <el-tag type="success">标签二</el-tag>
                    <el-tag type="info">标签三</el-tag>
                </div>
                <el-col :span="6">
                    <div class="grid-content">
                        <img src="../assets/img/postimg.jpg" alt="文章图片"></div>
                </el-col>
                <el-col :span="17" class="post-content">
                    <div class="">
                        <h2>这是文章的标题</h2>
                        <p v-text='msg'>
                        </p>
                        <div>
                            <el-row type="flex" class="row-bg" justify="end">
                                <el-col :span="4">
                                    <div class="">2018-2-2</div>
                                </el-col>
                                <el-col :span="4">
                                    <div class="">浏览(120)</div>
                                </el-col>
                                <el-col :span="4">
                                    <div class="">评论(10)</div>
                                </el-col>
                                <el-col :span="4">
                                    <div class=""><i class="iconfont icon-aixin"></i>(10)</div>
                                </el-col>
                            </el-row>
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
        props: ["num"],
        data: function() {
            return {
                msg: ''
            }
        },
        created: function() {
            this.msg = '这是一篇很长的文很长的文很的文很长的文很文很的文很文很长的文很长的文很文很长的文很长的文很文很长的文很长的文很文很长的文很长的文很长的文很长的文很长的文很长的文很长的文很长的文很长的文很长的文章'
        },
        mounted: function() {
            //90字符
            if (this.msg.length >= 90) {
                this.msg = this.msg.slice(0, 90) + '...'
            }
        }
    };
</script>


<style scoped>
    /*  */
    .post-tag {
        padding: 0 10px 10px 10px;
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
</style>
