// 这是文章列表视图
<template>
    <div class="post-list">
        <el-main>
            <!-- 列表头 -->
            <h2 style="margin:20px 15px;padding-bottom:10px;border-bottom:1px solid #ccc;">列表头</h2>
            <post-item :data="data"></post-item>
            <!-- 分页 -->
            <pagenation></pagenation>
        </el-main>
    </div>
</template>

<script>
// @ is an alias to /src
import Pagenation from '@/components/Pagenation.vue'
import PostItem from '@/components/PostItem.vue'

export default {
  data() {
    return {
      data: []
    }
  },
  created: function() {
    // 文章数据
    var postdata = [
      {
        postId: '1',
        imgUrl: '#',
        title: '文章的标题',
        description: '这是一段文章的简介',
        author: 'tempt',
        time: '2017-2-6',
        viewNum: '100',
        commentNum: '7',
        thumbs: '10',
        label: ['label1', 'label2']
      },
      {
        postId: '2',
        imgUrl: '#',
        title: '文章的标题2',
        description: '这是一段文章的简介',
        author: 'tempt',
        time: '2017-6-3',
        viewNum: '100',
        commentNum: '6',
        thumbs: '11',
        label: ['label1', 'label2']
      },
      {
        postId: '3',
        imgUrl: '#',
        title: '文章的标题3',
        description: '这是一段文章的简介',
        author: 'tempt',
        time: '2017-5-6',
        viewNum: '100',
        commentNum: '5',
        thumbs: '12',
        label: ['label1', 'label2']
      }
    ]
    this.data = postdata
    console.log(this.data)
  },
  components: {
    pagenation: Pagenation,
    'post-item': PostItem
  }
}
</script>

<style scoped>
/* 演示 */
.post-list {
  margin: 10px;
  width: 100%;
}
.el-main {
  padding: 0 10px;
}
</style>
