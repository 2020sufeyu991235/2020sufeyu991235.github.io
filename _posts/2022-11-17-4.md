---
title: Element的Layout布局
authod: cotes
date: 2022-11-17 23:22:00 +0800
categories: [Element]
tags: [Layout]
---

>更多请参考Element UI官方文档<https://element.eleme.cn/#/zh-CN/>
{: .prompt-tip}

<br>

## 24分栏
>Element中，`<el-row>`表示一行，`<el-col>`表示行内的分栏，`span`值表示分栏的宽度，行内span总和要等于24.
{: .prompt-tip}

```html
<el-row>
    <el-col :span="12"><div></div></el-col>
    <el-col :span="12"><div></div></el-col>
    <!--row内col的span可随意组合，但总和要等于24-->
</el-row>
```

<br>

## 分栏间隔
>`<el-row>`标签的`gutter`属性值表示每一栏间的间隔，默认间隔为0.
{: .prompt-tip}

```html
<el-row :gutter="20">
    <el-rol :span="16"><div></div></el-rol>
    <el-rol :span="8"><div></div></el-rol>
</el-row>
```

<br>

## 分栏偏移
>`<el-col>`标签的`offset`属性值表示分栏左侧的间隔距离，可以理解为左侧填充的空白分栏宽度。
{: .prompt-tip}

```html
<el-row :gutter="20">
    <el-col :span="6" :offset="6"><div></div></el-col>
    <el-col :span="6" :offset="6"><div></div></el-col>
</el-row>
```

<br>

## 对齐方式
>将`<el-row>`的`type`属性赋值为"flex"，可以启动flex布局，同时通过`justify`属性来指定子元素的排版方式。
{: .prompt-tip}

- justify可选值
  - start：左对齐,无间隔
  - center：居中对齐，无间隔
  - end：右对齐，无间隔
  - space-between：自适应间隔，边界无空白间隔
  - space-around：自适应间隔，边界有空白间隔

```html
<el-row type="flex" justify="center">
    <el-col :span="6"><div></div></el-col>
    <el-col :span="6"><div></div></el-col>
</el-row>
```

>看到这里你可能会疑惑，vue组件的属性有的要加冒号`:`，而有的不用，该如何判断？
{: .prompt-tip}
- 加冒号的
: 属性值为变量或表达式
- 不加冒号的
: 属性值为字符串字面量

<br>

## 响应式布局
>响应式布局就是在不同屏幕分辨率的终端上浏览同一个网页时会有不同展示方式，比如手机和电脑看到的网页布局肯定是要不同的。
{: .prompt-tip}

- Element提供了五个响应尺寸
  - xl：大于等于1920px
  - lg：大于等于1200px
  - md：大于等于992px
  - sm：大于等于768px 
  - xs：小于768px

```html
<el-row gitter="10">
    <el-col :xs={span:4,offset:4} :sm="6" :md="4" :lg="3" :xl="1"><div></div></el-col>
</el-row>
```

<br>

## 隐藏类
>Element提供了隐藏类用于在不同尺寸时隐藏元素，避免遮挡页面内容。这些类名可以添加在任何DOM元素或自定义组件上。另外使用需引入以下文件：
{: .prompt-tip}

```html
import 'element-ui/lib/theme-chalk/display.css';
```

- 类名&含义
  - hidden-xs-only - 当视口在 xs 尺寸时隐藏
  - hidden-sm-only - 当视口在 sm 尺寸时隐藏
  - hidden-sm-and-down - 当视口在 sm 及以下尺寸时隐藏
  - hidden-sm-and-up - 当视口在 sm 及以上尺寸时隐藏
  - hidden-md-only - 当视口在 md 尺寸时隐藏
  - hidden-md-and-down - 当视口在 md 及以下尺寸时隐藏
  - hidden-md-and-up - 当视口在 md 及以上尺寸时隐藏
  - hidden-lg-only - 当视口在 lg 尺寸时隐藏
  - hidden-lg-and-down - 当视口在 lg 及以下尺寸时隐藏
  - hidden-lg-and-up - 当视口在 lg 及以上尺寸时隐藏
  - hidden-xl-only - 当视口在 xl 尺寸时隐藏

<br>

## 速览
- `<el-row>`
  - gutter：分栏间隔
  - type：布局类型，flex
  - justify：flex布局下的水平排列方式
    - start：左对齐,无间隔
    - center：居中对齐，无间隔
    - end：右对齐，无间隔
    - space-between：自适应间隔，边界无空白间隔
    - space-around：自适应间隔，边界有空白间隔
    - align：flex布局下的垂直排列方式

- `<el-col>`
  - span：分栏占据的列数
  - offset：分栏左侧的间隔列数
  - push：分栏向右移动列数
  - pull：分栏向左移动列数
  - xl：1920px
  - lg：[1200,1920)
  - md：[992,1200)
  - sm：[768,992)
  - xs：768px