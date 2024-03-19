# Traefik

启动服务
```shell
docker-compose up -d
```

停止服务
```shell
docker-compose down
```

> 注意：本地记得修改hosts
```
127.0.0.1 test.cuiwei.net traefik.console.lab.io whoami.docker.localhost
```

## 控制台
http://traefik.console.lab.io


## 同时支持http和https
https://test.cuiwei.net/

http://test.cuiwei.net/

## 负载均衡
http://whoami.docker.localhost

```shell
  services:
    whoami-service:
      loadBalancer:
        servers:
          - url: "http://whoami:80/"
          - url: "http://test:80/"
```

Weighted Round Robin
```shell
  services:
    whoami-service:
      weighted:
        services:
          - name: appv1
            weight: 3
          - name: appv2
            weight: 1
    appv1:
      loadBalancer:
        servers:
          - url: "http://whoami:80/"
    appv2:
      loadBalancer:
        servers:
          - url: "http://test:80/"
```