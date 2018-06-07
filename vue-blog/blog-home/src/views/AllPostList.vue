// 这是文章列表视图
<template>
  <div class="post-list">
    <el-main>
      <!-- 列表头 -->
      <h2 style="margin:20px 15px;padding-bottom:10px;border-bottom:1px solid #ccc;">文章列表</h2>
      <post-item :data="data.slice((currentPage-1)*pagesize,currentPage*pagesize)"></post-item>
      <!-- 分页 -->
      <div>
        <el-pagination background layout="prev, pager, next" :total="total" :page-size="pagesize" @current-change="current_change">
        </el-pagination>
      </div>
    </el-main>
  </div>
</template>

<script>
// @ is an alias to /src
import PostItem from '@/components/PostItem.vue'

export default {
  data() {
    return {
      data: [],
      total: 0, //默认数据总数
      pagesize: 7, //每页的数据条数
      currentPage: 1 //默认开始页面
    }
  },
  created: function() {
    let _this = this
    this.axios
      .get('http://humorliang.top:5000/api/v_1.0/post/', {
        params: {
          all: Date.now()
        }
      })
      .then(function(response) {
        _this.data = JSON.parse(response.data)
        _this.total = _this.data.length
        // console.log(_this.total)
      })
      .catch(function(response) {
        console.log(response.data)
      })
  },
  components: {
    'post-item': PostItem
  },
  methods: {
    // 点击触发的回调函数，返回当前的页数也就是currentPage的值
    current_change: function(currentPage) {
      this.currentPage = currentPage
    }
  }
}
</script>

<style scoped>
/* 演示 */
.post-list {
  margin: 10px;
  width: 100%;
}
.el-main {
  padding: 0 10px;
}
</style>
