<template>
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
            <el-footer >版权信息&copy;2017|by龙在江湖设计|<router-link to="">管理员登陆</router-link></el-footer>
        </el-container>

    </div>
</template>




//
<script>
export default {};
</script>

//
<style scoped>
.el-footer{
    text-align: center;
}
.el-main h3{
    margin: 0;
    color: rgb(86, 151, 129);
}
.el-main .el-col .el-tag{
    margin: 5px;
}
</style>
