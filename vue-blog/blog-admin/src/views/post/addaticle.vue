<template>
  <div>
    <el-form ref="form" label-width="90px">
      <el-form-item label="文章标题">
        <el-col :span="10">
          <el-input></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="文章封面图">
        <el-col :span="10">
          <el-upload class="upload-demo" ref="upload" action="" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList" :auto-upload="false">
            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
          </el-upload>
        </el-col>
      </el-form-item>
      <el-form-item label="创作时间">
        <el-col :span="5">
          <el-date-picker v-model="formInline.date" type="date" placeholder="创作日期" style="width: 100%;"></el-date-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="文章分类">
        <el-select placeholder="请选择分类" v-model="formInline.value">
          <el-option label="分类1" value="javascript"></el-option>
          <el-option label="分类2" value="python"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="文章作者">
        <el-col :span="5">
          <el-input></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="文章简介">
        <el-col :span="10">
          <textarea name="post-info" id="post-info" cols="60" rows="10"></textarea>
        </el-col>
      </el-form-item>
    </el-form>
    <div>
      <!-- 编辑器 -->
      <h2 style="color:#676;padding-left:20px;margin-bottom:0;margin-top:30px;">文章正文：</h2>
      <editor-bar></editor-bar>
      <div>
        <el-button type="primary" @click="onSubmit" col="10">发表文章</el-button>
        <el-button>取消</el-button>
      </div>
    </div>
  </div>
</template>

<script>
//导入编辑器组件
import editor from '@/components/editor.vue'
export default {
  data() {
    return {
      formInline: {
        // 接受选择表单的数据
        value: '',
        date: ''
      },
      fileList: []
    }
  },
  components: {
    'editor-bar': editor
  },
  methods: {
    onSubmit() {
      console.log('submit!')
    },
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    }
  }
}
</script>
<style scoped>
</style>
