<template>
    <div>
        <el-col :span="24">
            <el-menu  class="el-menu-vertical-demo" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                <el-submenu index="1">
                    <template slot="title">
                        <i class="el-icon-tickets"></i>
                        <span>最新文章</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="1-1">文章一</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
                <el-submenu index="2">
                    <template slot="title">
                        <i class="el-icon-loading"></i>
                        <span>随机推荐</span>
                    </template>
                    <el-menu-item-group>
                        <el-menu-item index="2-1">文章1</el-menu-item>
                    </el-menu-item-group>
                </el-submenu>
            </el-menu>
        </el-col>
    </div>
</template>


<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
    //   console.log(key, keyPath)
    },
    handleClose(key, keyPath) {
    //   console.log(key, keyPath)
    },
    handlePostList2() {
     
    },
    handlePostList() {
      
    },
    handlePostCon() {
     
    }
  }
}
</script>


<style scoped>
</style>
