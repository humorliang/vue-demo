<template>
  <div id="app">
   <div>{{msg}}</div>
  </div>
</template>

<script>
//vue组件使用export default进行导出
export default {
  data: function() {
    return {
      msg: "todolist"
    };
  }
};
</script>

<style>
</style>
