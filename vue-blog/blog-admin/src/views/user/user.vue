<template>
    <div>
        <div>
            <el-row :gutter="10">
                <el-col :span="4">
                    <el-input placeholder="请输入内容"></el-input>
                </el-col>
                <el-button type="primary" icon="el-icon-search">搜索</el-button>
            </el-row>
        </div>
        <div>
            <el-table :data="tableData" style="width: 100%">
                <el-table-column type="index" width="50">
                </el-table-column>
                <el-table-column label="邮箱" width="280">
                    <template slot-scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.mail }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="用户名" width="280">
                    <template slot-scope="scope">
                        <span style="margin-left: 10px">{{ scope.row.name }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
      tableData: [
        {
          mail: '123@163.com',
          name: '小米'
        },
        {
          mail: '232@163.com',
          name: '小王'
        }
      ]
    }
  },
  methods: {
    handleDelete(index, row) {
      this.$confirm('是否真的删除这个用户？', '提示', {
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
