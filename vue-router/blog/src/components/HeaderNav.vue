<template>
    <div>
        <div>
            <router-link to="/">首页</router-link>
            <router-link to="#">电影</router-link>
            <router-link :to="{name:'music'}">音乐</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>

</style>