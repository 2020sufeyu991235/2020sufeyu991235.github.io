---
title: Vue+ElementUI+Webpack模板搭建项目
authod: cotes
date: 2022-11-18 18:17:00 +0800
categories: [Vue,Element]
---

>非完整教程，需有以下配置：
{: .prompt-warning}

- 安装好Nodejs
- 全局安装vue-cli(npm install -g vue-cli)

<br>

## 项目搭建
- - -
### 获取管理员权限。
  1. 以管理员身份运行cmd。
  2. 输入盘符。(参考 "d:")
  3. 打开相应目录。(项目存放目录，参考 "cd D:\Vue")

<br>

### 使用webpack模板搭建项目。
```
//初始化项目
vue init webpack-simple 项目名

//确认项目信息

//进入项目目录
cd 项目名

//构建
npm install

//运行
npm run dev
```

<br>

### 安装Element UI
```
//先ctrl+c，输入y退出。

//在项目中安装Element UI
npm install element-ui -S

//安装vue-router(路由)和vue-resource(执行Ajax请求用到的依赖)
npm install vue-router vue-resource --S

//实际操作出现了依赖冲突的问题，好像是vue版本冲突？暂时执行以下代码安装
npm install vue-router vue-resource --S --legacy--peer-deps

```
>全局安装和局部安装
{: .prompt-tip}
- npm install vue-cli -g
: `-g`表示全局安装，安装路径是Node安装目录下的node_modules文件夹。

- npm install element-ui -S
: `-S`表示局部安装，安装路径是当前项目的node_modules文件夹。

<br>

## 项目结构
- - -
### index.html
>很显然，这是一个html页面的骨架，由后续vue组件填充。
{: .prompt-tip}

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>vue_elementui</title>
  </head>
  <body>
    <div id="app"></div>
    <!--当前项目没有该文件，因为执行"npm run dev"生成的build.js是在内存中的-->
    <!--执行"nmp run build"会将生成的build.js发布到此路径上-->
    <script src="/dist/build.js"></script>
  </body>
</html>
```

<br>

### main.js
>我们在这里添加代码以引入Element。
{: .prompt-tip}

```js
import Vue from 'vue'
//导入APP.vue组件
import App from './App.vue'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

new Vue({
  //让当前vue对象绑定index.html上的<div id="app">元素
  el: '#app',
  //让App.vue的内容展现在<div>上
  render: h => h(App)
})
```

<br>

### App.vue
>APP.vue这种以".vue"为扩展名的文件，是我们需要构建页面的所在，index.html通过这样的Vue组件渲染就成为我们看到的网页。Vue组件的结构如下：
{: .prompt-tip}

```vue
<!--html-->
<template>
    <div></div>
</template>

<!--js-->
<script>
export default{
    //对象名
    name: 'app',

    //数据，比如处理后台传回的数据
    data(){
        return{
            msg: 'Welcome to Your Vue.js App'
        }
    },

    //方法
    methods:{},

    //计算属性
    computed:{},

    //监听
    watch:{}
}
</script>

<!--css-->
<style></style>
```

<br>

## 开始学习
- - -
>vue组件中使用Element组件时发生错误，提示：
{: .prompt-warning}

```
ERROR in ./node_modules/element-ui/lib/theme-chalk/fonts/element-icons.ttf
Module parse failed: Unexpected character '' (1:0)
...
```

>在`webpack.config.js`中添加配置：(参考<https://blog.csdn.net/qq_52855464/article/details/125299092>)
{: .prompt-tip}

```js
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
        loader: 'file-loader'
      }
    ]
```

<br>

>然后开始官方组件文档的学习，跳转<https://element.eleme.cn/#/zh-CN/>
{: .prompt-tip}