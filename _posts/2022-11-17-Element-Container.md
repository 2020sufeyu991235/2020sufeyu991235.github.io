---
title: Element的Container布局容器
authod: cotes
date: 2022-11-18 23:22:00 +0800
categories: [Element]
---

>更多请参考Element UI官方文档<https://element.eleme.cn/#/zh-CN/>
{: .prompt-tip}

<br>

## 开始
>用于布局的容器组件，方便快速搭建页面的基本结构：
{: .prompt-tip}

- `<el-container>`：外层容器。当子元素包含`<el-header>`或`<el-footer>`时，全部子元素会垂直上下排列，否则水平左右排列。
  - `<el-header>`：顶栏容器。
  - `<el-aside>`：侧边栏容器。
  - `<el-main>`：主要区域容器。
  - `<el-footer>`：底栏容器。

<br>

>在App.vue测试了一个简单的布局：(复杂的布局有点迷惑，后面再搞)
{: .prompt-tip}

```vue
<template>
  <div id="app">
    <!--header-->
    <el-container style="height: 65px; border:2px solid #eee">
      <el-header>
        <a href="#">header</a>
      </el-header>
    </el-container>

    <!--aside和main-->
    <el-container style="height: 500px">
      <el-aside style="border:2px solid #eee">
        <a href="#">aside</a>
      </el-aside>
      <el-main style="border:2px solid #eee">
        <a href="#">main</a>
      </el-main>
    </el-container>

    <!--footer-->
    <el-container>
      <el-footer style="border:2px solid #eee">
        <a href="#">footer</a>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {}
}
</script>

<style></style>
```

<br>

## 速览
- `<el-container>`
  - direction：子元素的排列方向。
    - horizontal：水平方向
    - vertical：垂直方向
    - 子元素中有`<el-header>`或`<el-footer>`时为vertical，否则为horizontal
- `<el-header>`
  - height：默认60px
- `<el-aside>`
  - width：默认300px
- `<el-main>`
- `<el-footer>`
  - height：默认60px