<template>
  <div>
    <div>
      <el-row :gutter="10">
        <el-col :span="4">
          <el-input placeholder="请输入内容"></el-input>
        </el-col>
        <el-button type="primary" icon="el-icon-search">搜索</el-button>
        <el-button type="primary" icon="el-icon-plus" @click="toArticle">新建文章</el-button>
      </el-row>
    </div>
    <el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)" style="width: 100%">
      <el-table-column label="ID" type="index" width="50">
      </el-table-column>
      <el-table-column prop="date" label="文章日期" width="120">
      </el-table-column>
      <el-table-column prop="author" label="作者" width="120">
      </el-table-column>
      <el-table-column prop="title" label="标题">
      </el-table-column>
      <el-table-column label="分类" width="160">
        <template slot-scope="scope">
          <el-tag size="samll" type="success">{{scope.row.kind}}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">
            编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row,scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 分页 -->
    <div>
      <el-pagination background layout="prev, pager, next" :total="total" :page-size="pagesize" @current-change="current_change">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [],
      total: 0, //默认数据总数
      pagesize: 7, //每页的数据条数
      currentPage: 1 //默认开始页面
    }
  },
  // 拿数据
  created() {
    let _this = this
    this.axios
      .get('http://humorliang.top:5000/api/v_1.0/post/')
      .then(function(response) {
        // console.log(response.data)
        _this.tableData = JSON.parse(response.data)
        _this.total = _this.tableData.length
      })
      .catch(function(err) {
        console.log(err.data)
      })
  },
  methods: {
    toArticle() {
      this.$router.push({ name: 'addarticle' })
    },
    handleEdit(index, row) {
      console.log(index, row)
    },
    handleDelete(index, row, id) {
      console.log(index, row)
      this.$confirm('是否真的删除这篇文章？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
        center: true
      })
        .then(() => {
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          this.tableData.splice(index, 1)
          this.axios
            .delete('http://humorliang.top:5000/api/v_1.0/post/?post_id=' + id)
            .then(function(response) {
              console.log(response.data)
            })
            .catch(function(err) {
              console.log(err.data)
            })
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      this.$router.push({ name: 'post', params: { t: Date.now() } })
    },
    // 点击触发的回调函数，返回当前的页数也就是currentPage的值
    current_change: function(currentPage) {
      this.currentPage = currentPage
    }
  },
}
</script>
