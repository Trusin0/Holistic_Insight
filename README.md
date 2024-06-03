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
