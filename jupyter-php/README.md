# Jupyter Notebook 安装 PHP 内核

## docker 部署
构建和运行
```shell
docker build -t registry.cn-hangzhou.aliyuncs.com/cuiw/php-jupyter:8.1.9-fpm-v1.1 .

docker run -d --name php-jupyter -p 8888:8888 registry.cn-hangzhou.aliyuncs.com/cuiw/php-jupyter:8.1.9-fpm-v1.1
```

## 详见
https://github.com/Rabrennie/jupyter-php-kernel

https://www.cuiwei.net/p/1391718888