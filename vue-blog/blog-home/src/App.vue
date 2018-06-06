<template>
    <div id="app">
        <el-container>
            <!-- 头部 -->
            <el-header>
                <div>
                    <el-menu class="el-menu-demo" mode="horizontal" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                        <div style="float: left;height: 60px;margin-right: 100px;line-height: 60px;">
                            <img src="./assets/img/logo.png" alt="龙在江湖" class="logo" style="height: 80%;vertical-align: middle;"></div>
                        <el-menu-item index="1">首页</el-menu-item>
                        <el-submenu index="2">
                            <template slot="title">前端厨房
                            </template>
                            <el-menu-item index="2-1">案例小菜</el-menu-item>
                            <el-menu-item index="2-2">踩坑指南</el-menu-item>
                        </el-submenu>
                        <el-submenu index="3">
                            <template slot="title">
                                后端囧事
                            </template>
                            <el-menu-item index="3-1">服务器</el-menu-item>
                            <el-menu-item index="3-2">数据库</el-menu-item>
                        </el-submenu>
                        <el-submenu index="4">
                            <template slot="title">数据爬虫
                            </template>
                            <el-menu-item index="4-1">案例堆场</el-menu-item>
                        </el-submenu>
                        <el-menu-item index="5">
                            来撩我
                        </el-menu-item>
                    </el-menu>
                </div>
            </el-header>
            <!-- 中部 -->
            <el-container>
                <el-aside width="300px">
                    <div>
                        <el-col :span="24">
                            <el-menu class="el-menu-vertical-demo" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
                                <el-submenu index="1">
                                    <template slot="title">
                                        <i class="el-icon-tickets"></i>
                                        <span>文章分类</span>
                                    </template>
                                    <el-menu-item-group>
                                        <el-menu-item v-for="item of kinddata" :key="item.kind_id" index="1-1">{{item.kind_name}}</el-menu-item>
                                    </el-menu-item-group>
                                </el-submenu>
                                <el-submenu index="2">
                                    <template slot="title">
                                        <i class="el-icon-loading"></i>
                                        <span>随机推荐</span>
                                    </template>
                                    <el-menu-item-group>
                                        <el-menu-item v-for="item of randompost" :key="item.post_id" index="2-1">{{item.title}}</el-menu-item>
                                    </el-menu-item-group>
                                </el-submenu>
                            </el-menu>
                        </el-col>
                    </div>
                </el-aside>
                <!-- 视图挂载点 -->
                <router-view/>
            </el-container>
            <!-- 底部 -->
            <el-footer>
                <div>
                    <el-container>
                        <el-main>
                            <el-row>
                                <el-col :span="12">
                                    <h3>友情链接：</h3>
                                    <div class="">
                                        <el-tag type="success">标签二</el-tag>
                                        <el-tag type="info">标签三</el-tag>
                                        <el-tag type="warning">标签四</el-tag>
                                        <el-tag type="danger">标签五</el-tag>
                                    </div>
                                </el-col>
                                <el-col :span="12">
                                    <div class="">
                                        <h3>联系我：</h3>
                                        <div class="">
                                            <el-tag type="success">邮箱</el-tag>
                                            <el-tag type="info">微信</el-tag>
                                            <el-tag type="warning">Github</el-tag>
                                        </div>
                                    </div>
                                </el-col>
                            </el-row>
                        </el-main>
                        <el-footer style="text-align:center; font-size:14px;">版权信息&copy;2017|by龙在江湖设计|
                            <router-link to="">管理员登陆</router-link>
                        </el-footer>
                    </el-container>
                </div>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
export default {
  data() {
    return {
      kinddata: '',
      randompost: ''
    }
  },
  created() {
    let _this = this
    this.axios
      .get('http://127.0.0.1:5000/api/v_1.0/kind/')
      .then(function(response) {
        _this.kinddata = JSON.parse(response.data)
        // console.log(_this.kinddata)
      })
      .catch(function(err) {
        console.log(err.data)
      })
    this.axios
      .get('http://127.0.0.1:5000/api/v_1.0/post/', {
        params: {
          random_num: 3
        }
      })
      .then(function(response) {
        _this.randompost = JSON.parse(response.data)
        console.log(_this.randompost)
      })
      .catch(function(err) {
        console.log(err.data)
      })
  }
}
</script>

<style lang="stylus">
body {
    margin: 0;
}

header.el-header {
    padding: 0;
}

#app {
    min-width: 1200px;
}
</style>
