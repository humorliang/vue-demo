<template>
    <div>
        <h1>赶紧留言来撩我吧</h1>
        <msg-board></msg-board>
    </div>
</template>

<script>
    import Comment from "../components/Comment.vue";
    export default {
        components: {
            "msg-board": Comment
        }
    }
</script>

<style scoped>
h1{
    text-align: center;
    color: aquamarine
}
</style>