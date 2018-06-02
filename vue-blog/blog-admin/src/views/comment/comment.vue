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
                <el-table-column label="文章标题" width="220">
                    <template slot-scope="scope">
                        <span>{{ scope.row.title }}</span>
                    </template>
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
          title: '文章标题',
          username: '夏明',
          time: '2018-5-6',
          commentInfo: '这是评论的内容',
          status: '待审核',
          ip: '192.16.1.1'
        },
        {
          title: '文章标题',
          username: 'lim',
          time: '2018-5-6',
          commentInfo: '这是评论的内容',
          status: '待审核',
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
