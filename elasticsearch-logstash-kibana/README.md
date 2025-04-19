# 文章
[http://www.cuiwei.net/p/1886813055](http://www.cuiwei.net/p/1886813055)


## 设置密码
进入es容器执行, `-i`为自定义密码

### 设置es密码
```
// es123456
elasticsearch@elasticsearch:~$ elasticsearch-reset-password -u elastic -i
```

### kibana链接es的密码
```
// es123456
elasticsearch@elasticsearch:~$ elasticsearch-reset-password -u kibana_system -i
```

### 进阶，证书验证
#### es
```
//生成证书颁发机构 elastic-stack-ca.p12，密码空
./bin/elasticsearch-certutil ca

//生成证书 elastic-certificates.p12，密码空
./bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12

//移到指定目录
cp elastic-certificates.p12 config/
```
#### kibana
使用连接器需要安全配置
```
./bin/kibana-encryption-keys generate

xpack.encryptedSavedObjects.encryptionKey: 27bcf13b552f2cdff57102a942b271a6
xpack.reporting.encryptionKey: 3a1d4358ef9f7965d4095dbc3d6c6986
xpack.security.encryptionKey: 45e47452ca6f12f24011e8e15f6e2e7f
```

## logstash
### GeoLite2
这里用到了`GeoLite2`，通过ip地址获取国家，地区，经纬度等信息

需要手动下载：https://github.com/wp-statistics/GeoLite2-City

文件保存在这个位置：`logstash/GeoLite2-City.mmdb`

### 调试
```
logstash -e 'input {

}
filter {
  geoip {
    target => "geoip"
    source => "ip"
    database => "/usr/share/logstash/GeoLite2-City.mmdb"
    fields => ["city_name", "region_name", "country_name"]
  }
}
output { stdout {} }
' --path.data /tmp
```

## elastalert2
### 安装，使用
普通安装
```
pip3.13 install elastalert2 --index-url https://pypi.org/simple

//启动
python3.13 -m elastalert.elastalert --verbose --config /opt/elastalert/elastalert.yaml 

//创建索引
python3.13 -m elastalert.create_index --config /opt/elastalert/elastalert.yaml
```

### 其他
`-U`参数，安装最新版本，包括相关依赖
```
pip3.13 install -U elastalert2 --index-url https://pypi.org/simple
```

```
  Could not find a version that satisfies the requirement prettytable>=3.8.0 (from elastalert2) (from versions: 0.3, 0.4, 0.5, 0.6, 0.6.1, 0.7.1, 0.7.2, 1.0.0, 1.0.1, 2.0.0, 2.1.0, 2.2.0, 2.2.1, 2.3.0, 2.4.0, 2.5.0)
No matching distribution found for prettytable>=3.8.0 (from elastalert2)

#更新包缓存
pip3.13 install -U stomp.py --index-url https://pypi.org/simple
```

## 参考
https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

https://github.com/clay584/logstash_configs/blob/master/logstash.conf