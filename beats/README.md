Beats 是轻量型数据采集器，Beats 是一个免费且开放的平台，集合了多种单一用途数据采集器。它们从成百上千或成千上万台机器和系统向 Logstash 或 Elasticsearch 发送数据。

# 启动服务
```
docker-compose up -d
```

# 推荐使用Linux系统

metricbeat
> 特殊文件系统/proc和/sys仅在主机系统运行Linux时可用。尝试绑定装载这些文件系统将在Windows和macOS上失败。

packetbeat
> 在Windows和MacOS上，指定--network=host将把容器的网络接口绑定到Docker嵌入式Linux虚拟机的虚拟接口，而不是与主机系统的物理接口绑定。

# 文章
http://www.cuiwei.net/p/1590183676