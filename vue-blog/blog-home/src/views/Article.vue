<template>
  <div class="post-con">
    <!-- 文章的内容 -->
    <el-container>
      <el-main>
        <!-- 二级视图挂载点 -->
        <el-card class="box-card">
          <div slot="header" class="post-title">
            <h1>{{postdata.title}}</h1>
            <el-row type="flex" justify="center">
              <el-col :span="6">作者：{{postdata.author}}</el-col>
              <el-col :span="6">时间：{{postdata.time}}</el-col>
            </el-row>
          </div>
          <div v-html="postdata.content">
          </div>
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import AsideNav from '@/components/AsideNav.vue'
export default {
  data() {
    return {
      postdata: {
        author: '1',
        time: '1',
        content: '1',
        title: '1'
      }
    }
  },
  created() {
    // console.log(this.$route.params.id) //{id: 37}
    var id = this.$route.params.id
    let _this = this
    this.axios
      .get('http://humorliang.top:5000/api/v_1.0/post/', {
        params: { post_id: id }
      })
      .then(function(response) {
        _this.postdata = JSON.parse(response.data)
        // console.log(response.data)
      })
      .catch(function(err) {
        console.log(err.data)
      })
  },
  components: {
    'aside-nav': AsideNav,
    'comment-bar': Comment
  },
  watch: {
    // 对路由进行监视，变化就更新数据
    $route(to, from) {
      var id = this.$route.params.id
      let _this = this
      this.axios
        .get('http://humorliang.top:5000/api/v_1.0/post/', {
          params: { post_id: id }
        })
        .then(function(response) {
          _this.postdata = JSON.parse(response.data)
          // console.log(response.data)
        })
        .catch(function(err) {
          console.log(err.data)
        })
    }
  }
}
</script>

<style scoped>
h1 {
  margin: 0 0 20px;
}
.post-con {
  width: 100%;
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