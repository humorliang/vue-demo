<template>
    <div>
        我是英文歌曲
        传过来的id为{{id}}
    </div>
</template>

<script>
export default {
  data() {
    return {
      id: this.$route.query.id
    };
  }
};
</script>

<style scoped>
</style>