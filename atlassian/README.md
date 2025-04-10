## 常见问题
自 Confluence 8.6 起，新版本仅支持 Data Center 许可证。
官方可下载的最新[8.5](https://www.atlassian.com/zh/software/confluence/download-archives) 版本是 `8.5.21`，但官方docker镜像只到 [8.5.6](https://hub.docker.com/r/atlassian/confluence-server/tags?name=8.5.6)

自 Jira Software 9.13 起，新版本仅支持 Data Center 许可证。
官方可下载的最新[9.12](https://www.atlassian.com/zh/software/jira/download-archives) 版本是 `9.12.20`，官方docker镜像也支持 [9.12.20](https://hub.docker.com/r/atlassian/jira-core/tags?name=9.12.20)

1. 设置事务级别 RC
```
transaction-isolation=READ-COMMITTED

#给my.cnf设置644
chmod 644 /etc/my.cnf
#重启mysql
```

2. 安装后markdown文章无法显示

随便选一个免费的 markdown 编辑器 安装即可

3. 新版本Confluence（8.5.6）重置管理员密码(/opt/atlassian/confluence/bin/setenv.sh) 不可用（添加完，服务重启失败，无解！）
```
vi /opt/atlassian/confluence/bin/setenv.sh
CATALINA_OPTS="-Datlassian.recovery.password=12345678"
```

4. 备份恢复
   1. 安装一个全新的系统（admin/admin888）
   2. 进入后台恢复备份文件 `./confluence/data/restore/site/xmlexport-20250406-141007-1.zip`
   3. 登录admin账号（admin/admin888）,安装一个免费的markdown插件

## 文章
https://www.cuiwei.net/p/1258785919

https://www.cuiwei.net/p/1825498777

