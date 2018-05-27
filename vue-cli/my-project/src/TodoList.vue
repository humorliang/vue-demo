<template>
  <div>
   <div>
     <input type="text" v-model="inputValue">
     <button @click="handleClick">提交</button>
   </div>
   <!-- 子组件的使用 -->
   <!-- 父组件向子组件传递值通过属性 -->
   <!-- 父组件监听子组件的事件 -->
   <todo-item v-for="(item,index) of list" 
   :key="index" 
   :content='item' 
   :index='index'
   @delete='handleDelete'></todo-item>
  </div>
</template>

<script>
//导入子组件
import TodoItem from "./components/TodoItem";
//vue组件使用export default进行导出
export default {
  // 注册子组件
  components: {
    // 怎样的方式使用子组件
    "todo-item": TodoItem
  },
  data: function() {
    return {
      inputValue: "",
      list: []
    };
  },
  methods: {
    handleClick() {
      this.list.push(this.inputValue);
      this.inputValue = "";
    },
    handleDelete(index) {
      this.list.splice(index, 1);
    }
  }
};
</script>

<style>
</style>
