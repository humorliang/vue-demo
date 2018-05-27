<template>
<div>
    <div @click="handleDelete">{{content}}</div>
</div>
</template>

<script>
export default {
    //通过props接受父组件的传值
    props:['content','index'],
    methods:{
        handleDelete(){
            //子组件通过自定事件向父组件传值 $emit('事件名','执行事件函数时接受的参数')
            this.$emit('delete','index')
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
