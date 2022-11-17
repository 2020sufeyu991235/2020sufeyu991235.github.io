---
title: (windows)将Chirpy站点部署到Github Pages
authod: cotes
date: 2022-11-17 17:07:00 +0800
categories: [Jekyll]
tags: [Chirpy]
---

>非完整教程，以下操作在windows系统上进行，部署之前需有以下配置：
{: .prompt-warning}

- 安装Ruby+devkit。(我安装的是rubyinstaller-devkit-2.5.9-1-x64，推荐2.5.9版本，最新版本安装Jekyll有未知的错误)
- 安装git。(Ruby好像会自带，但自己下一个比较好，后续要用到Git Bash)
- 安装Jekyll。(gem install jekyll bundler)
- 建立远程仓库，默认分支名为main或master。(注意后续项目文件要推送到默认分支)
- 克隆远程仓库到本地，导入Chirpy模板(即已经下载好Chirpy模板文件到本地仓库)，**以下配置在本地仓库路径的cmd命令行完成**：(即在仓库路径栏输入cmd运行)
  - 执行bundle install成功(安装Chirpy需要的依赖文件)
  - 执行bundel exec jekyll s成功(在本地预览正常)

<br>

## 删除部分文件
>在本地仓库路径右键点击Git Bash Here。
{: .prompt-tip}

>执行以下命令。注意做好手动备份，尤其是_posts下的文件将被删除。
{: .prompt-danger}

```
bash tools/init.sh
```

<br>

## 更新Gemfile.lock
>Gemfile.lock里面记录的是项目所需要的依赖文件列表(猜的)，因为本地依赖是适应windows系统的，但github pages部署网站使用的是Linux系统(生成静态页面在github上运行)，所以要添加适应Linux系统的文件列表。在本地仓库路径的cmd命令行(即在仓库路径栏输入cmd运行)输入命令：
{: .prompt-tip}

```
bundle lock --add-platform x86_64-linux
```

<br>

## 修改Github Pages部署执行的yml文件
  1. 用vscode或记事本打开pages-deploy.yml文件，路径为.github\workflows\pages-deploy.yml
  2. 找到以下代码
  ```yml
  - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: 3 # reads from a '.ruby-version' or '.tools-version' file if 'ruby-version' is omitted
          bundler-cache: true
  ```
  修改ruby-version为本地使用的ruby版本。(打开一个新的cmd输入：ruby -v查看。参考格式：2.5.9)

<br>

## Github Pages配置
  1. 在github上点击Settings，再点击Pages
  2. Build and deployment下的Source选择Github Actions
  3. 如果有自定义域名并且DNS解析正常，可以在Custom domain下填入。

<br>

## 上推远程仓库
  1. 使用git将本地仓库上推到远程仓库。
  2. 上推成功后，查看github的Actions的最新一个运行是否成功，如果成功了，等一会搜索下自定义域名或github pages给的域名(xxxx.github.io)；如果不成功，查看Actions里的报错(可展开查看)，然后加油解决。

<br>

## 其他
>部署成功离让其真正成为你的个人博客还有一点距离，你需要把文件里(比如_comfig.yml)的信息修改为自己的信息，总之，加油吧！
{: .prompt-tip}

## 最后
>因为这篇博客是在搞定一切问题之后才有的，所以有什么纰漏请不要怪罪(虽然小破站也没什么人看)。如果这篇博客不能解决你的问题(我能体会那种抓狂的感觉)，作为过来人我只能说，**一定要看明白报错的提示**，以及多看官方文档和issues。(官方链接<https://github.com/cotes2020/jekyll-theme-chirpy/>)
{: .prompt-tip}