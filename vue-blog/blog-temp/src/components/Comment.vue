<template>
    <div>
        <el-card class="box-card">
            <div slot="header">
                <span>留言信息</span>
            </div>
            <div>
                <el-row>
                    <el-col :span="24">
                        <el-input type="textarea" :rows="3" placeholder="请输入内容">
                        </el-input>
                    </el-col>
                </el-row>
                <el-row>
                    <el-button type="success" size="small" plain>发表留言</el-button>
                </el-row>
            </div>
            <div class="comment-list">
                <div v-for="o in 4" :key="o" class="item">
                    <li>
                        <div class="profile"><img src="../assets/img/postimg2.jpg" alt=""></div>
                        <div class="msg">
                            <div class="msg-body">
                                <p class="name">张三 <span class="date">2018-6</span></p>
                                <p> 这世界评论的内容</p>
                            </div>
                        </div>
                    </li>
                </div>
            </div>
        </el-card>
    </div>
</template>

<script>
    export default {
    }
</script>

<style scoped>
    .comment-list {
        margin-top: 20px;
    }
    .comment-con {
        margin-bottom: 10px;
    }
    .comment-con .el-row {
        border-bottom: 1px solid #ccc;
        padding-bottom: 10px;
    }
    li {
        list-style: none;
        text-align: left;
        overflow: hidden;
        margin-bottom: 2em;
        padding: 0.4em;
    }
    .profile {
        width: 80px;
        float: left;
    }
    .profile img {
        border-radius: 50%;
        border: 2px solid #fff;
        width: 48px;
        height: 48px;
        background-color: #ddd;
        box-shadow: 0 0 5px #ddd;
    }
    .msg {
        width: 86%;
        float: left;
        background-color: #fff;
        border-radius: 0 5px 5px 5px;
        box-shadow: 0 4px 8px -2px rgba(0, 0, 0, 0.05);
        position: relative;
    }
    .msg-body {
        padding: 0.8em;
        color: #666;
        line-height: 1.5;
    }
    .msg-body p:last-child {
        margin-bottom: 0;
    }
    .msg-body:after {
        content: " ";
        position: absolute;
        left: -13px;
        top: 0;
        border: 14px solid;
        border-color: #fff transparent transparent transparent;
    }
    .name {
        margin: 0;
        color: #999;
        font-weight: bold;
        font-size: 0.8em;
    }
    .date {
        float: right;
    }
</style>