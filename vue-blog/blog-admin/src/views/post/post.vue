<template>
    <div>
        <div>
            <el-row :gutter="10">
                <el-col :span="4">
                    <el-input placeholder="请输入内容"></el-input>
                </el-col>
                <el-button type="primary" icon="el-icon-search">搜索</el-button>
                <el-button type="primary" icon="el-icon-plus">新建文章</el-button>
            </el-row>
        </div>
        <el-table :data="tableData" style="width: 100%">
            <el-table-column label="ID" type="index" width="50">
            </el-table-column>
            <el-table-column prop="date" label="文章日期" width="180">
            </el-table-column>
            <el-table-column prop="name" label="作者" width="120">
            </el-table-column>
            <el-table-column prop="address" label="标题">
            </el-table-column>
            <el-table-column label="标签">
                <template slot-scope="scope">
                    <el-tag v-for="(o,index) of scope.row.label" :key="index" size="mini" type="success">{{o}}</el-tag>
                </template>
            </el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">
                        编辑</el-button>
                    <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        {
          date: '2016-05-02',
          name: 'tempt',
          address: '这是文章的标题',
          label: ['label1', 'label2']
        },
        {
          date: '2016-05-04',
          name: 'tempt',
          address: '这是文章的标题',
          label: ['label1', 'label2']
        },
        {
          date: '2016-05-01',
          name: 'tempt',
          address: '这是文章的标题',
          label: ['label1', 'label2']
        },
        {
          date: '2016-05-03',
          name: 'tempt',
          address: '这是文章的标题',
          label: ['label1', 'label2']
        }
      ]
    }
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row)
    },
    handleDelete(index, row) {
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
