采用分阶段构建，减小镜像体积
```
git clone git@github.com:tal-tech/alarm-dog-fe.git
cd alarm-dog-fe
mv .env.production .env

#构建镜像
docker build -t chudaozhe/alarm-dog-fe:1.0.0-v1.1 .
```