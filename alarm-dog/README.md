# 哮天犬告警平台

哮天犬是一个通用的统一告警平台，提供配置化、流程化、标准化的能力。可以选择对接日志中心日志类监控、实时计算类的监控能力，各业务方也可以直接在代码中埋点上报告警，同时我们团队也可以定制化开发既能满足业务需求又能快速复用告警平台的监控系统，实现监控告警全场景覆盖。
[使用文档](https://www.yuque.com/tal-tech/alarm-dog)

## 开始使用

```
# 根据实际情况修改各目录中的 .env 文件，其中 alarm-dog-fe 需要重新构建，步骤详见alarm-dog-fe/README.md

# 启动docker
docker-compose up -d

# 导入sql
docker exec -it alarm-dog_mysql_1 /bin/bash
cd /data
mysql -p (password: root)
create database alarm_dog;
use alarm_dog;
source alarm_dog.sql;

# 导入clickhouse
docker exec -it alarm-dog_clickhouse_1 /bin/bash
cd /data
clickhouse-client
create database alarm_dog;
use alarm_dog;
source clickhouse.sql;
#或者把sql去掉空格，换行，然后加分号，最后复制sql粘贴执行
```

默认账号：admin 密码：alarm-dog

## 模块介绍

仓库名称 | 模块名称 | 模块介绍
--- | --- | ---
alarm-dog-admin | 后台接口 | 提供后台管理接口服务和开放平台接口服务，一般内网解析
alarm-dog-fe | 后台web界面 | 提供后台管理界面服务，前后端分离
alarm-dog-api | 告警接口 | 提供告警接口服务，一般公网解析
alarm-dog-consumer | 告警消费 | 对告警接口产生的告警消息进行消费，实现非常丰富的告警功能
alarm-dog-monitor | 监控模块 | 哮天犬不做监控，但想抽象出一系列的监控模型，这是一个监控探索模块
alarm-dog-noticer | 消息通知SDK | 提供各模块消息通知功能，包括后台邮件发送、告警接口自监控告警发送、告警消费告警发送等
alarm-dog-php-sdk | PHP告警SDK | 对告警接口封装，提供PHP语言快速接入能力
alarm-dog-golang-sdk | Golang告警SDK | 对告警接口封装，提供Golang语言快速接入能力
alarm-dog-java-sdk | Java告警SDK | 对告警接口封装，提供Java语言快速接入能力
alarm-dog-docs | 使用文档 | 提供文档使用说明
