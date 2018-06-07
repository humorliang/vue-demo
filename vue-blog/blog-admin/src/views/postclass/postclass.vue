<template>
  <div>
    <div>
      <el-row :gutter="10">
        <el-button type="primary" icon="el-icon-plus" @click="addKind">添加分类</el-button>
      </el-row>
    </div>
    <div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column type="index" width="50">
        </el-table-column>
        <el-table-column label="类名" width="280">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.kind_name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="文章数" width="280">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.post_num }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row,scope.row.kind_id)">
              删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      // tableData:null 显示暂无数据
      tableData: []
      //分类检验变量
    }
  },
  // 拿数据
  created() {
    let _this = this
    this.axios
      .get('http://humorliang.top:5000/api/v_1.0/kind/')
      .then(function(response) {
        // console.log(response.data)
        _this.tableData = JSON.parse(response.data)
        // console.log(_this.tableData)
      })
      .catch(function(error) {
        console.log(error)
      })
  },
  methods: {
    //添加
    addKind() {
      // 数据更新
      // 找个变量接受vue实例，以便内部访问
      let _this = this
      this.$prompt('分类名', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        //   inputValidator进行校验
        inputValidator(value) {
          // value输入的参数
          for (let i = 0; i < _this.tableData.length; i++) {
            // console.log(Boolean(_this.tableData[i]['kind_name'] == value))
            if (_this.tableData[i]['kind_name'] == value) {
              return false
            }
          }
        },
        inputErrorMessage: '分类名已存在'
      })
        .then(({ value }) => {
          this.$message({
            type: 'success',
            message: '添加: ' + value + ' 分类成功'
          })
          this.axios
            .post('http://humorliang.top:5000/api/v_1.0/kind/?name=' + value)
            .then(function(response) {
              console.log(response)
              // 添加成功后刷新数据
              _this.axios
                .get('http://humorliang.top:5000/api/v_1.0/kind/')
                .then(function(response) {
                  // console.log(response.data)
                  _this.tableData = JSON.parse(response.data)
                  // console.log(_this.tableData)
                  _this.$router.push({ name: 'kind' })
                })
                .catch(function(error) {
                  console.log(error)
                })
            })
            .catch(function(error) {
              console.log(error)
            })
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '取消输入'
          })
        })
    },
    // 删除
    handleDelete(index, row, id) {
      this.$confirm('是否真的删除这个分类吗？分类下的文章都会被删除！', '提示', {
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
          // this.tableData.splice(index, 1)
          let _this = this
          console.log(id)
          this.axios
            .delete('http://humorliang.top:5000/api/v_1.0/kind/?id=' + id)
            .then(function(response) {
              // console.log(response)
              if (response.status == 200) {
                _this.tableData.splice(index, 1)
              }
            })
            .catch(function(error) {
              console.log(error)
            })
          // console.log(kind_id)
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
    }
  }
}
</script>


<style scoped>
</style>
