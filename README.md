# JableTVDownload

## 下載JableTV好幫手
项目基于 https://github.com/hcjohn463/JableTVDownload 修改而来，从使用chrome_driver、selenium 的方式改成了使用 browserless、playwright

服务启动后会每天请求一次分类页，下载没有下载的视频

需要有一个可以访问的 browserless 容器，使用 docker 搭建 browserless 非常方便

``` docker run -dit --name browserless -p 3000:3000 browserless/chrome ```

修改 app.yaml，配置文件有详细注释，一般不用改。除非你有特殊的需求：比如有 N 卡 做 ffmpeg 的转码加速，比如对影片的分类有特殊偏好

## 简单的安装：
创建一个容器，挂载相应的媒体存储目录

``` docker run -dit --name jab -V xxxx:/media nikolaik/python-nodejs ```

进入容器安装依赖

``` apt update && apt intall git ```

``` npm install -g pm2 ```

``` git clone https://github.com/LeanFly/JableTVDownloader ```

进入代码目录，安装依赖，启动服务

``` cd JableTVDownloader```

``` pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple```

``` pm2 start app.py --interpreter=python3 ```


