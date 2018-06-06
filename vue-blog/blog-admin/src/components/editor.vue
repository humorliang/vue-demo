<template>
    <div>
        <div ref="editor" style="text-align:left;z-index:10 !important;"></div>
    </div>
</template>

<script>
// 导入富文本wangeditor
import E from 'wangeditor'
export default {
  name: 'editor',
  data() {
    return {
      editorContent: ''
    }
  },
  methods: {
    getContent: function() {
      alert(this.editorContent)
    }
  },
  mounted() {
    //实例化编辑器类
    var editor = new E(this.$refs.editor)
    editor.customConfig.onchange = html => {
    //文本编辑器的内容为html格式并赋值
      this.editorContent = html
    }
    // 初始化编辑器
    editor.create()
  }
}
</script>

<style scoped>

</style>