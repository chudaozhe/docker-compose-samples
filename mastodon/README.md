# Docker 部署 Mastodon - 一个去中心化的社交平台

## 开始之前

准备一个域名和证书

- 域名：`test.cuiwei.net`
- 证书：`test.cuiwei.net.key`、`test.cuiwei.net.pem`

如果只是想本地跑一下，也行

- 修改hosts：`127.0.0.1 test.cuiwei.net`
- web、streaming、sidekiq 这3个服务增加`extra_hosts`，如下：

```
extra_hosts: 
  - "test.cuiwei.net:192.168.11.241"

#192.168.11.241 为宿主机ip
#extra_hosts作用是 往容器内/etc/hosts文件中添加记录，注意格式是相反的
```

## 快速开始

### 初始化
```
docker compose -f docker-compose.yml run --rm web bundle exec rake mastodon:setup
```

上一步执行成功，会启动`db`和`redis`两个容器，同时会提示你输入域名（先别输），先进到`db`容器创建一个给`mastodon`用的数据库，如下创建一个用户和数据库，名称都是`mastodon`，密码为空
```
psql -U postgres
CREATE USER mastodon CREATEDB;
create database mastodon owner mastodon encoding UTF8;
```

接着，按照提示，一步步来

![169908382570482.jpg](https://www.cuiwei.net/data/upload/2023-11-04/169908382570482.jpg)

接下来，生成一份配置，需要手动复制到`.env.production`文件

![169908382556411.jpg](https://www.cuiwei.net/data/upload/2023-11-04/169908382556411.jpg)

最后是导入数据，和创建管理员用户

![169908382571691.jpg](https://www.cuiwei.net/data/upload/2023-11-04/169908382571691.jpg)


### 启动服务
初始化完成，就能启动服务了
```
docker compose up -d
```

## 访问
https://test.cuiwei.net


## 其他
1. `.env.production` 从何而来？

下载官方代码
```
git clone git@github.com:mastodon/mastodon.git
```
根目录有个`.env.production.sample`文件，改名为 `.env.production`，(必须的)

如果是初次运行，记得把里面`LOCAL_DOMAIN`, `PostgreSQL`，`redis`这些你知道的都配好（不配也可以，只是最后一步创建管理员账号会失败）
