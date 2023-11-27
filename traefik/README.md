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
127.0.0.1 test.cuiwei.net
```

## 同时支持http和https
https://test.cuiwei.net/

http://test.cuiwei.net/

## 负载均衡

```shell
  services:
    whoami-service:
      loadBalancer:
        servers:
          - url: "http://whoami:80"
          - url: "http://test:80"
```
```shell
  services:
    whoami-service:
      loadBalancer:
        strategy: LeastConnections
        servers:
          - url: "http://whoami:80"
          - url: "http://test:80"
```

```shell
  services:
    whoami-service:
      loadBalancer:
        strategy: WeightedRoundRobin
        servers:
          - url: "http://whoami:80"
            weight: 1
          - url: "http://test:80"
            weight: 3
```