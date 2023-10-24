采用分阶段构建，减小镜像体积
```
git clone git@github.com:tal-tech/alarm-dog-fe.git
cd alarm-dog-fe
mv .env.production .env

#修改.env中的变量，如：
VUE_APP_BASE_API = '//www.alarm-dog.com/api/'
VUE_APP_STATIC_PREFIX = '//www.alarm-dog.com/admin/'
#无需加端口号，详见../alarm-nginx.conf

#拿alarm-dog-fe/Dockerfile覆盖原来的Dockerfile文件

#构建镜像
docker build -t registry.cn-hangzhou.aliyuncs.com/cuiw/alarm-dog-fe:1.0.0-v1.1-production1 .
```