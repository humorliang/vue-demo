<template>
    <div>
        <el-form label-position="left" label-width="0px" class="demo-ruleForm login-container">
            <h3 class="title" style="text-align:center; color:rgb(58, 202, 113)">系统登录</h3>
            <el-form-item>
                <i class="iconfont icon-zhanghao i-postion"></i>
                <el-input type="text" auto-complete="off" placeholder="账号" class="padding-left">
                </el-input>
            </el-form-item>
            <el-form-item>
                <i class="iconfont icon-xiugaimima i-postion" style="font-size:28px; left:-16px;"></i>
                <el-input type="password" auto-complete="off" placeholder="密码" class="padding-left"></el-input>
            </el-form-item>
            <el-checkbox checked class="remember">记住密码</el-checkbox>
            <el-form-item style="width:100%;">
                <el-button type="primary" style="width:100%;">登录</el-button>
                <!--<el-button @click.native.prevent="handleReset2">重置</el-button>-->
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {};
</script>


<style scoped>
    .i-postion {
        position: absolute;
        left: -11px;
        top: 0;
        font-size: 20px;
        color: rgb(58, 202, 113);
        z-index: 100;
    }
    .el-form-item {
        position: relative;
    }
    .padding-left {
        padding-left: 10px;
    }
    .login-container {
        /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
        -webkit-border-radius: 5px;
        border-radius: 5px;
        -moz-border-radius: 5px;
        background-clip: padding-box;
        margin: 180px auto;
        width: 350px;
        padding: 35px 35px 15px 35px;
        background: #c0e2e1;
        border: 1px solid #eaeaea;
        box-shadow: 0 0 25px #cac6c6;
        .title {
            margin: 0px auto 40px auto;
            text-align: center;
            color: #505458;
        }
        .remember {
            margin: 0px 0px 35px 0px;
        }
    }
</style>
