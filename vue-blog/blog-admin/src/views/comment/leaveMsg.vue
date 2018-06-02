<template>
    <div>
        <div>
            <el-table :data="tableData" style="width: 100%">
                <el-table-column type="index" width="50">
                </el-table-column>
                <el-table-column label="用户名" width="120">
                    <template slot-scope="scope">
                        <span>{{ scope.row.username }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="时间" width="180">
                    <template slot-scope="scope">
                        <span>{{ scope.row.time }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="状态" width="100">
                    <template slot-scope="scope">
                        <span>{{ scope.row.status }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="IP地址" width="150">
                    <template slot-scope="scope">
                        <span>{{ scope.row.ip }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="内容" width="180">
                    <template slot-scope="scope">
                        <el-popover trigger="click" placement="top">
                            <p>{{ scope.row.username }}: {{ scope.row.commentInfo }}</p>
                            <div slot="reference" class="name-wrapper">
                                <el-tag size="medium" class="pointer">查看</el-tag>
                            </div>
                        </el-popover>
                    </template>
                </el-table-column>
                <el-table-column label="操作">
                    <template slot-scope="scope">
                        <el-button size="mini" type="primary" v-if="scope.row.status=='待审核'">通过</el-button>
                        <el-button size="mini" type="danger" v-if="scope.row.status=='通过'" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
          username: '夏明',
          time: '2018-5-6',
          commentInfo: '这是评论的内容',
          status: '待审核',
          ip: '192.16.1.1'
        },
        {
          username: 'lim',
          time: '2018-5-6',
          commentInfo: '这是评论的内容',
          status: '通过',
          ip: '192.16.1.1'
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
.pointer {
  cursor: pointer;
}
</style>
