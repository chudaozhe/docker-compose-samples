nextcloud + postgres
# 启动服务
```
docker-compose up -d
```

注意：postgres初始化成功会创建 用户名`nextcloud`，数据库`nextcloud`，密码`nextcloud`，详见`./data/apps/postgresql/source/init-user-db.sh`

注意：`docker-compose.yml`中关于`docker-nextcloud`的配置，里面的环境变量是没起作用的。正常情况配置了这些变量就能实现自动配置（访问入口页，无需手动填写数据库信息），不过也可以手动下载`https://github.com/nextcloud/docker/tree/master/23/fpm-alpine/config` 这个`config`目录，复制到安装目录下，以实现自动配置

# 备份
nc镜像中包含了整个项目，首次无法映射到主机
```
docker exec -it docker-nextcloud /bin/sh
/var/www/html # cd ..
/var/www # tar -cvzf backup/html.tar.gz html/
```
# 文章
http://www.cuiwei.net/p/1477777115
