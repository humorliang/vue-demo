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
                        <span style="margin-left: 10px">{{ scope.row.name }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="文章数" width="280">
                    <template slot-scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.num }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">
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
      tableData: [
        {
          name: 'javascript',
          num: '10'
        },
        {
          name: 'javascript',
          num: '20'
        }
      ]
    }
  },
  methods: {
    //添加
    addKind() {
      this.$prompt('分类名', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消'
        //   inputValidator进行校验
        // inputValidator(){
        //     return 'error'
        // },
        //   inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        //   inputErrorMessage: '分类名已存在'
      })
        .then(({ value }) => {
          this.$message({
            type: 'success',
            message: '添加: ' + value + ' 分类成功'
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
    handleDelete(index, row) {
      this.$confirm('是否真的删除这个分类吗？', '提示', {
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
