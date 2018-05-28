## vue-router使用笔记
### vue-router使用方式
- 1:下载vue-router 方式 'npm i vue-router -S'
- 2:在入口main.js中引用 "import VueRouter form 'vue-router'"
- 3:在vue的根实例文件中安装插件 'Vue.use(VueRouter)' 挂载属性
- 4:创建路由对象并配置路由规则
    + 'const router=new VueRouter({routes: [ {path:'/home',
    component:Home} ]})'
- 5:将其路由对象传递给Vue实例，option中
    + option中加入 'router:router'
- 6:在app.vue中留坑 '<router-view></router-view>'

* 路由理解：
    根据不同的路由进行不同的组件渲染，留一个坑对应的就渲染一个组件，多个坑
    对应多个组件。
### router-link的使用
- 1：使用router-link进行路由跳转
    + '<router-link :to='{name:'home'}'></router-link>'
- 2: 使用router-link对象传递参数
    * 使用字符串查询的方式/home?id=xxx&name=xxx
    + '<router-link :to='{ name:'home',query:{id:'1',name:'sudu2'} }'></router-link>'
    * 使用params方式/home/1
    + params方式在路由规则设置时要声明，而query则不需要
        {name:'home',path:'/home/:id',component:Home}
    + '<router-link :to='{ name:'home',params:{id:'1'} }'></router-link>' 
- 3:获取传递的参数
    * 利用vue的钩子函数
    ```javascript
        //Dom还没有生成
        created(){
            //获取路由参数
            //vue-router挂载两个对象的属性挂载到实例this上
            //$route(信息数据) $router(功能函数)
            console.log(this.$route.query)
            console.log(this.$route.params)
        }
    ```
### 多视图
* 多个视图就有多个坑
    * 根组件中的视图挂载设置
    ```html
        <router-view name="header"/>
        <router-view /> <!--默认的名字为  default-->
        <router-view name="footer"/>
    ```
    * 路由规则设置
    ```javascript
        routes: [
        {
        path: '/',
        components: {
            //使用坑名应用组件
            header:HeaderNav,
            default:MainContent,
            footer:FooterNav
        }}]
    ```
