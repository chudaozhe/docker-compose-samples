# Jupyter Notebook 安装 PHP 内核

## docker 部署
构建和运行
```shell
docker build -t registry.cn-hangzhou.aliyuncs.com/cuiw/php-jupyter:8.1.9-fpm-v1.1 .

docker run -d --name php-jupyter -p 8888:8888 registry.cn-hangzhou.aliyuncs.com/cuiw/php-jupyter:8.1.9-fpm-v1.1
```

## 开始
```
网页版：

http://127.0.0.1:8888/

或者，配合VS Code使用：

打开一个.ipynb文件，右上角选择内核，选择Jupyter服务器:


获取token
cat /root/.local/share/jupyter/runtime/jupyter_cookie_secret 


http://127.0.0.1:8888/lab?token={token}

```
## 详见
https://github.com/Rabrennie/jupyter-php-kernel

https://www.cuiwei.net/p/1391718888