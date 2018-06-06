/* 这是主页视图 */
<template>
  <div class="home">
    <el-main>
      <!-- 调用列表项 -->
      <post-item :data="data"></post-item>
    </el-main>
  </div>
</template>

<script>
// @ is an alias to /src
import AsideNav from '@/components/AsideNav.vue'
import PostItem from '@/components/PostItem.vue'

export default {
  data() {
    return {
      data: []
    }
  },
  created: function() {
    let _this = this
    this.axios
      .get('http://127.0.0.1:5000/api/v_1.0/post/', {
        params: {
          limit: 3
        }
      })
      .then(function(response) {
        _this.data=JSON.parse(response.data)
        // console.log(_this.data)
      })
      .catch(function(response) {
        console.log(response.data)
      })
  },
  components: {
    'aside-nav': AsideNav,
    'post-item': PostItem
  }
}
</script>

<style scoped>
/* 演示 */
.el-main {
  padding: 0 10px;
}
.home {
  padding: 10px 0;
  width: 100%;
}
</style>
