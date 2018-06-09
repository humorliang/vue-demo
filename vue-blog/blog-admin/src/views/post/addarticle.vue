<template>
  <div>
    <el-form ref="dataForm" :model="dataForm" :rules="rules" label-width="90px">
      <el-form-item label="文章标题" prop='title'>
        <el-col :span="10">
          <el-input v-model="dataForm.title"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="文章封面图">
        <el-col :span="10">
          <el-upload class="upload-demo" ref="upload" action="#" :on-preview="handlePreview" :on-remove="handleRemove" :file-list="fileList" :auto-upload="false">
            <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
            <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
            <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过1000kb</div>
          </el-upload>
        </el-col>
      </el-form-item>
      <el-form-item label="创作时间" prop="date">
        <el-col :span="5">
          <el-date-picker v-model="dataForm.date" type="date" placeholder="创作日期" style="width: 100%;"></el-date-picker>
        </el-col>
      </el-form-item>
      <el-form-item label="文章分类" prop="kind">
        <el-select placeholder="请选择分类" v-model="dataForm.kind">
          <el-option v-for="(item,index) of dataForm.kind_list" :key="index" :label="item" :value="item"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="文章作者" prop="author">
        <el-col :span="5">
          <el-input v-model="dataForm.author"></el-input>
        </el-col>
      </el-form-item>
      <el-form-item label="文章简介" prop="desc">
        <el-col :span="10">
          <textarea name="post-info" id="post-info" cols="60" rows="10" v-model="dataForm.desc"></textarea>
        </el-col>
      </el-form-item>
    </el-form>
    <div>
      <!-- 编辑器 -->
      <h2 style="color:#676;padding-left:20px;margin-bottom:0;margin-top:30px;">文章正文：</h2>
      <div id="my-editor">
        <div ref="editor" style="text-align:left;z-index:10 !important;"></div>
      </div>
      <div>
        <!-- 这里的表单要使用引号 -->
        <el-button type="primary" @click="onSubmit('dataForm')" col="10">发表文章</el-button>
        <el-button>取消</el-button>
      </div>
    </div>
  </div>
</template>

<script>
// 导入富文本wangeditor
import E from 'wangeditor'
export default {
  data() {
    return {
      dataForm: {
        // 选择分类的数据
        kind_list: '',
        title: '',
        // 保存选择的分类数据
        kind: '',
        date: '',
        author: '',
        desc: '',
        content: ''
      },
      // 数据验证
      rules: {
        title: [
          { required: true, message: '请输入文章标题', trigger: 'blur' },
          { min: 3, max: 25, message: '长度在 3 到 25 个字符', trigger: 'blur' }
        ],
        kind: [{ required: true, message: '请选择分类', trigger: 'change' }],
        date: [
          {
            type: 'date',
            required: true,
            message: '请选择日期',
            trigger: 'change'
          }
        ],
        author: [{ required: true, message: '请输入作者', trigger: 'blur' }],
        desc: [{ required: true, message: '请输入文章描述', trigger: 'blur' }]
      },
      // 文件列表
      fileList: []
    }
  },
  created() {
    let _this = this
    this.axios
      .get('http://127.0.0.1:5000/api/v_1.0/kind/')
      .then(function(response) {
        var kindData = JSON.parse(response.data)
        var kind_name_list = []
        for (var i = 0; i < kindData.length; i++) {
          kind_name_list.push(kindData[i]['kind_name'])
        }
        //设置分类数据
        _this.dataForm.kind_list = kind_name_list
      })
      .catch(function(error) {
        console.log(error)
      })
  },
  mounted() {
    //实例化编辑器类
    var editor = new E(this.$refs.editor)
    editor.customConfig.onchange = html => {
      //文本编辑器的内容为html格式并赋值geied
      this.dataForm.content = html
    }
    // 初始化编辑器
    editor.create()
  },
  methods: {
    onSubmit(formName) {
      // 对表单控件进行验证
      this.$refs[formName].validate(valid => {
        if (valid) {
          // 验证成功
          // 日期处理函数
          function formatDate(date) {
            var d = new Date(date),
              month = '' + (d.getMonth() + 1),
              day = '' + d.getDate(),
              year = d.getFullYear()

            if (month.length < 2) month = '0' + month
            if (day.length < 2) day = '0' + day
            return [year, month, day].join('-')
          }
          //数据对象整理
          var postData = {
            title: this.dataForm.title,
            author: this.dataForm.author,
            date: formatDate(this.dataForm.date),
            kind: this.dataForm.kind,
            desc: this.dataForm.desc,
            content: this.dataForm.content
          }
          console.log(postData.date)
          this.axios
            .post('http://127.0.0.1:5000/api/v_1.0/post/', postData)
            .then(function(response) {
              console.log(response.data)
            })
            .catch(function(error) {
              console.log(error.data)
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
      // this.$router.push({ name: 'post', params: { t: Date.now() } })
      // console.log(this.dataForm)
    },
    submitUpload() {
      // 上传
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
