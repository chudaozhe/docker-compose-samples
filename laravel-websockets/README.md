
## docker-compose 快速部署 laravel-websockets

### 快速开始
启动服务
```
docker-compose up -d
```

### 构建过程
#### 曲折的过程
一开始我考虑基于`php:8.1.9-apache`镜像构建，这样除了`websocket`服务（6001端口），web控制台`http://localhost/laravel-websockets` （80端口）也由这个镜像提供。但是最后两个服务总有一个起不来，`Dockerfile CMD`部分如下
```
CMD apache2-foreground && php artisan websockets:serve
```

暂时无解，所以下面是基于`php:8.1.9-cli`镜像构建的过程

由于是尝试，所以我们不直接写`Dockerfile`，而是直接运行基础镜像（`php:8.1.9-cli`）
```
  docker-laravel-websockets:
    image: 'php:8.1.9-cli'
    ports:
      - '6001:6001'
    networks:
      - server_web-network
```

然后进入容器操作
```
cd /var/www
composer create-project laravel/laravel=9.* --prefer-dist app
cd app

#安装laravel-websockets

步骤请移步：https://www.cuiwei.net/p/1659113677

也需要配下id, key, secret和数据库连接

vi .env

PUSHER_APP_ID=12345
PUSHER_APP_KEY=ABCDEFG
PUSHER_APP_SECRET=HIJKLMNOP

DB_CONNECTION=mysql
DB_HOST=docker-mysql
DB_PORT=3306
DB_DATABASE=test
DB_USERNAME=root
DB_PASSWORD=

```

### 构建镜像
由上可得一个`Dockerfile`文件，构建一下就好了
```
cuiwei@weideMacBook-Pro docker-laravel-websockets % docker build -t chudaozhe/php:8.1.9-cli-laravel-websockets-v1.0 .
```