docker-nextcloud

postgres / mariadb二选一，默认 mariadb

注意：postgres初始化成功会创建 用户名`nextcloud`，数据库`nextcloud`，密码`nextcloud`，详见`./postgresql/source/init-user-db.sh`

# 启动服务
```
docker-compose up -d
```
# 访问
```
http://localhost
```

# 文章
http://www.cuiwei.net/p/1477777115