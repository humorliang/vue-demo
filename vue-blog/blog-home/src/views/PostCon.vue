<template>
    <div class="post-con">
        <!-- 文章的内容 -->
        <el-container>
            <el-aside width="300px">
                <!-- 侧边组件 -->
                <aside-nav></aside-nav>
            </el-aside>
            <el-container>
                <el-main>
                    <!-- 二级视图挂载点 -->
                    <el-card class="box-card">
                        <div slot="header" class="post-title">
                            <h1>{{title}}</h1>
                            <el-row type="flex" justify="center">
                                <el-col :span="6">作者：{{author}}</el-col>
                                <el-col :span="6">时间：{{time}}</el-col>
                            </el-row>
                        </div>
                        <div>
                            {{content}}
                        </div>
                    </el-card>
                    <comment-bar></comment-bar>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
import AsideNav from "@/components/AsideNav.vue";
import Comment from "@/components/Comment.vue";
export default {
  data() {
      return{
          author:'',
          time:'',
          content:'',
          title:''
      }
  },
  created(){
      this.author='tempt',
      this.time='2018-9-5',
      this.content='这是文章的的内容内容',
      this.title='这是一个牛逼的文章标题'
  },
  components: {
    "aside-nav": AsideNav,
    "comment-bar": Comment
  }
};
</script>

<style scoped>
h1 {
  margin: 0 0 20px;
}

.post-title {
  text-align: center;
}
.post-con > .el-container {
  padding: 10px;
}
.el-main {
  padding: 0 10px;
}
/* 留言 */
</style>