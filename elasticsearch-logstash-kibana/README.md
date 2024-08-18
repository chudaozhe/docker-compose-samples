# 文章
[http://www.cuiwei.net/p/1886813055](http://www.cuiwei.net/p/1886813055)


## 设置密码
进入es容器执行, `-i`为自定义密码

### 设置es密码
```
#GsAWSPUndOODvIhAuXJB
elasticsearch@elasticsearch:~$ elasticsearch-reset-password -u elastic
```

### kibana链接es的密码
```
elasticsearch@elasticsearch:~$ elasticsearch-reset-password -u kibana_system -i
```

## 参考
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html