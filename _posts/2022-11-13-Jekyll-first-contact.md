---
title: Jekyll初接触
authod: cotes
date: 2022-11-15 15:38:00 +0800
categories: [Jekyll]
render_with_liquid: false
---


# 1.jekyll的目录结构
- _layouts(页面布局模板)
- _sass(样式表)
- _includes(可以复用的html页面)
- _posts(存放博客)
- _site(展示的静态页面，博客生成的页面存放在这里)
- assers/style(原生的资源文件)
  - js
  - css
  - image
- _config.yml(全局配置文件)
- index.html(首页页面)

<br>

# 2._posts&编写博客
>_posts文件夹专门用于存放我们记录的博客。
{: .prompt-tip}

- 博客命名方式：年-月-日-标题.md
- 页首内容：
  - layout: 布局。使用官方提供布局(layout: single)或自定义布局(位于_layouts文件夹)。
    注意：有些主题会layout会设置默认，无需再手动写。
  - title: 文章标题
  - date: 最后更新时间
  - tags: 文章标签
  - categories: 文章分类

<br>

# 3.Liquid
>jekyll的模板基于Liquid语言，想要构建自己的模板需要学习下相关的知识。
{: .prompt-tip}

- - -
## 3.1.变量
>变量以{{variable}}的形式被嵌入页面中，在静态页面生成时会被替换成具体的数值。常用的全局变量对象如下：

- site：对应网站范围，自定义变量放在_config.yml中，如url: xxx，使用{{site.url}}获取数据。
- page：对应单个页面，自定义变量放在页面的最开头。
- content：在布局文件(_layouts)中使用，表示要呈现的内容。

<br>


# 4._layouts&自定义模板
## 4.1.post.html
>首先我们看下博客所引用的模板样例：post.html

~~~ html
---
layout: default <!--这里又引用了另外一个模板default.html-->
---

<!-- article：表示这是一个与上下文不相关的独立部分 -->
<!-- itemtype：属性项来自于后面的链接。itemprop：给内容添加一个属性项/标注。我的理解是提炼关键数据给搜索引擎用的，暂时不深入了解 -->
<article class="main-content page-page" itemscope itemtype="http://schema.org/Article">
    <div class="post-header">
        <h1 class="post-title" itemprop="name headline">
            {{ page.title }}
        </h1>
        <div class="post-data">
            <time itemprop="datePublished">{{ page.date | date: "%b %d, %Y" }}</time>
        </div>
    </div>
</article>

<div class="main-container">
    <div class="post-container">

        <!-- 目录 -->
        <div class="navigation" id="navigation">
            <h1>目录</h1>
            <ul class="nav sidenav"></ul>
        </div>

        <!-- 内容 -->
        <article class="post-content">
            {{ content }}
        </article>

        <!-- 评论 -->
        <div class="post-content">
         {% include comment.html %}
        </div>
    </div>
</div>
~~~

- - -

## 4.2.default.html
>我们接着看被引用的模板：default.html

~~~ html
<!DOCTYPE html>
<html>

  {% include head.html %}

<body class="bg-grey" gtools_scp_screen_capture_injected="true">

    {% include header.html %}

    {{ content }} <!-- content读取的内容就是post.html里的页面 -->
    
    {% include footer.html %}

</body>
</html>
~~~

>很明显，模板+引用在default.html中组成了一个完整的页面，这就是最终发布在github pages上的页面。
{: .prompt-tip }

<br>

# 5._includes&可复用页面
>我们再看下default.html里include的页面

- - -
## 5.1.head.html
>html的head部分

~~~ html
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1">
    <meta name="renderer" content="webkit">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta http-equiv="Cache-Control" content="no-transform"/>
    <meta http-equiv="Cache-Control" content="no-siteapp"/>
    <title>{{ page.title | default: site.name }}</title>
	<meta name="description" content="{{site.meta_description}}">
	<link rel="shortcut icon" href="{{ '/style/image/favicon.png' | prepend: site.baseurl }}">
    <link rel="apple-touch-icon" href="{{ '/style/image/favicon.png' | prepend: site.baseurl }}"/>
    <link href="{{ '/style/css/highlight.min.css' | prepend: site.baseurl }}" rel="stylesheet">
    <link href="{{ '/style/css/style.min.css' | prepend: site.baseurl }}" rel="stylesheet">
	<link rel="stylesheet" href="{{ '/style/css/iconfont/iconfont.css' | prepend: site.baseurl }}">
</head>
~~~

- - -

## 5.2.header.html
>顶部项目栏的选项

~~~ html
<header id="header" class="header bg-white">
    <div class="navbar-container">
        <a href="{{ '/' | prepend: site.baseurl }}" class="navbar-logo">
            <img src="{{ '/style/image/logo.png' | prepend: site.baseurl }}" alt="{{ site.name }}" />
            <span>{{ site.name }}</span>
        </a>
        <div class="navbar-menu">
            <a href="{{ '/archives' | prepend: site.baseurl }}">点滴</a>
            <a href="{{ '/about' | prepend: site.baseurl }}">关于</a>
        </div>
        <div class="navbar-mobile-menu" onclick="">
            <span class="icon-menu cross"><span class="middle"></span></span>
            <ul>
                <li><a href="{{ '/archives' | prepend: site.baseurl }}">点滴</a></li>
                <li><a href="{{ '/about' | prepend: site.baseurl }}">关于</a></li>
            </ul>
        </div>
    </div>
</header>
~~~

- - -

## 5.3.footer.html
>页尾

~~~ html
<footer id="footer" class="footer bg-white">
    <div class="footer-social">
        <div class="footer-container clearfix">
            <div class="social-list">
                <a href="{{ '/' | prepend: site.baseurl }}"><span class='iconfont icon-home'></span>&nbsp;&nbsp;HOME</a>
                <a rel="nofollow" target="_blank" href="{{site.github}}"><span class='iconfont icon-github'></span>&nbsp;&nbsp;Github</a>
                <a target="_blank" href="{{ '/feed.xml' | prepend: site.baseurl }}"><span class='iconfont icon-rss'></span>&nbsp;&nbsp;RSS</a>
            </div>
        </div>
    </div>
    <div class="footer-meta">
        <div class="footer-container">
            <div class="meta-item meta-copyright">
                <div class="meta-copyright-info">
                    <a href="{{site.resume_site}}" class="info-logo">
                        <img src="{{ '/style/image/logo.png' | prepend: site.baseurl }}" alt="wonder">
                    </a>
                    <div class="info-text">
                        <p>Copyright &copy; 2022 - {{ site.time | date: '%Y' }} <a href="{{site.resume_site}}"><code>{{ site.author }}</code></a></p>
                        <p>Powered by <a href="http://jekyllrb.com" target="_blank" rel="nofollow"><code>jekyll</code></a>，theme is <a href="https://github.com/lightfish-zhang/pinghsu-jekyll" target="_blank" rel="nofollow"><code>pinghsu</code></a></p>
                    </div>
                </div>
            </div>

            <div class="meta-item meta-posts">
                <h3 class="meta-title">RECENT POSTS</h3>
                {% for post in site.posts limit:7 %}
                    <li>
                        <a href="{{ post.url }}">{{ post.title }}</a>
                    </li>
                {% endfor %}
            </div>

        </div>
    </div>
</footer>

<!-- #end -->
<script src="//cdn.bootcss.com/jquery/1.10.1/jquery.min.js"></script>
<script>
	!window.jQuery && document.write(unescape('%3Cscript src="{{ site.baseurl }}/style/js/jquery.min.js"%3E%3C/script%3E'))
</script>
<script src="{{ site.baseurl }}/style/js/headroom.min.js"></script>
<script src="{{ site.baseurl }}/style/js/nav.min.js"></script>
<script type="text/javascript">
    var header = new Headroom(document.getElementById("header"), {
        tolerance: 10,
        offset : 80,
        classes: {
            initial: "animated",
            pinned: "slideDown",
            unpinned: "slideUp"
        }
    });
    header.init();
</script>

<script>window.SmoothScrollOptions = { stepSize: 36 }</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/smoothscroll/1.4.8/SmoothScroll.min.js"></script>
<script>
	!window.SmoothScroll && document.write(unescape('%3Cscript src="{{ site.baseurl }}/style/js/SmoothScroll.min.js"%3E%3C/script%3E'))
</script>

{% if site.googlaAnalyticsID %}
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', '{{site.googlaAnalyticsID}}', 'auto');
  ga('send', 'pageview');
</script>
{% endif %}
~~~

<br>

# 6.style&页面布局
>这里没有深入了解，看了看模板2000多行的css代码，突然感觉自己没有修改模板的能力(虽然模板看着很好看，但想添加一些功能或调整一些样式)，再看看。

<br>

# 7.在线预览&生成静态文件
>经过一番了解，不免想要写一篇博客尝试一下(已经安装Ruby和Jekyll)，但在此之前还需要一些准备工作。

- - -
## 7.1.filehandler.rb
参照<https://blog.csdn.net/Btbsja/article/details/104607079>添加代码。

- - -
## 7.2.代码块
>要使markdown的```或~~~生效，需修改_config.yml局部配置如下：
{: .prompt-tip }

```
markdown: kramdown
kramdown:
  input: GFM
```
>同时因为博客的代码块里有Liquid语法，有如下办法使其不生效：

- 在博客顶部加入render_with_liquid: false。Jekyll需4.0以上，但不知道为什么我用的没有效果。
- 使用{% raw %}{% endraw %}将含有Liquid语法的所有代码囊括起来(用一对即可)。

- - -
## 7.3.在线预览
- 在1.中目录的路径栏输入cmd，执行代码bundle exec jekyll server
- 在浏览器输入localhost:4000(输入自己对应的端口)即可在线预览。
- 如果要停止，同时按ctrl+c，然后连续输入Y即可停止。

>注意：开启服务时，修改博客会自动更新生成的静态页面，只需刷新浏览器即可看到新页面。
{: .prompt-tip }