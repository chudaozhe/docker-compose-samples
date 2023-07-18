
## docker-compose 快速部署 JumpServer

第一步，修改`.env`配置mysql，redis连接信息，持久化存储目录，及web访问端口

第二步，初始化
```
# 注意看日志，迁移文件执行完成后，再执行下一步
docker-compose up -d core
```

第三步，启动其他容器，如果某个启动失败，可手动重试
```
docker-compose up -d
```

最后，打开 http://localhost:8099 ，即可访问管理后台。用户名，密码默认都是`admin`

## 参考

https://github.com/jumpserver/Dockerfile

https://www.cuiwei.net/p/1444551885
