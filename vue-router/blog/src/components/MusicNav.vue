<template>
    <div>
        <router-link :to="{name:'music_china',query:{id:'12'}}">中文</router-link>
        <router-link :to="{name:'music_english',query:{id:'13'}}">英文</router-link>
        <router-view></router-view>
        我在音乐视图主页
    </div>
</template>

<script>
export default {};
</script>

<style scoped>
</style>