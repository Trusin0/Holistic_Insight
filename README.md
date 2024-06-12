### 关于修改代码
## ！！！！！！请务必将代码推送到自己的分支上，不要直接在master分支上进行修改！！！！！！


### 怎么让项目跑起来？
目前我们的项目还没有使用到**backend**的服务，所以你暂时不需要考虑后端的相关内容，只是尝试着把前端页面跑起来。

首先，你需要安装好 Node.js 环境，如果你从未安装过npm，那么请按照下面的步骤进行：

1. 使用 node 自带的 npm 包管理器安装 vue 和相关模块。推荐使用淘宝的 cnpm 命令行工具代替默认的 npm。

```
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

2. 安装 vue.js。
```
cnpm install -g vue
```

3. 安装vue-cli脚手架工具（vue-cli是官方脚手架工具，能迅速帮你搭建起vue项目的框架）
```
cnpm install -g vue-cli
```

4. 安装 vue 依赖模块
```
cd frontend
cnpm install
cnpm install vue-resource
cnpm install element-ui
```

完成了上面的内容后，你应该已经成功安装了npm和vue，但是对于我们的项目，还需要在python中安装一些额外的依赖库：

你可能需要运行下面的指令，但是并不排除由于网络or镜像源的问题导致安装失败，这个需要你自己想办法：
```
pip install django-cors-headers
```

如果你成功安装了这些依赖库，那么你就可以运行下面的命令构建前端项目了：
```
cd frontend
npm run build
```
上面的指令在frontend的README中也有写。

最后，你需要启动一个本地服务器，让前端项目跑起来。你可以使用下面的命令：

```
python manage.py runserver 8000
```

然后你就可以在浏览器中访问 http://localhost:8000 看到我们的项目了。

### 项目架构是怎么样的？
虽然现在看来项目的架构非常的庞大，但是实际上你只需要关注一小部分的内容：
1. frontend/src 这个文件夹存放了几乎所有的资源，如果你是前端的coder，那么你需要着重关注这个
文件夹，首先，components目录下存放了一些公用的组件（如header、footer等），这些组件几乎会出现在所有
页面中。
2. src/views 这个文件夹存放了所有的页面，主要是index（游戏索引），game（目前只创建了一个reactionTime），
后面还需要添加Login、Register、Profile等页面。
3. src/router 这个文件夹存放了路由，主要是index.js和routes.js，index.js是入口文件，routes.js是路由配置文件。
4. src/App.vue 这个文件是整个项目的根组件，它是所有页面的父组件，它包含了页面的头部和底部，以及页面的主要内容。

### 如何添加前端页面？
请参照views/index下的架构，编写一个类似的vue页面，并将它添加到路由中。你不需要关注topbar和bottombar，这些组件已经在App.vue中定义好了。

在编写vue界面的过程中，你可能会频繁求助于大模型，但是大模型生成的代码会将所有的组件放置在同一个文件下，这
会导致代码的可读性变差，且整个文件非常的笨重，所以建议你将组件分离到不同的文件中，参照index下的架构。

好了，你可以开始干活了。

![img.png](img.png)