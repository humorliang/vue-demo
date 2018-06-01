<template>
    <div>
        <div>
            <el-row>
                <el-col :span="24">
                    <el-input type="textarea" :rows="3" placeholder="请输入内容">
                    </el-input>
                </el-col>
            </el-row>
            <el-row>
                <el-button type="success" size="small" plain @click="send_msg">发表留言</el-button>
            </el-row>
        </div>
    </div>
</template>

<script>
    export default {
        methods:{
            send_msg(){
                this.$emit('clickSend','data');
            }
        }
    };
</script>

<style scoped>

</style>