FROM atlassian/jira-core:9.4.0-jdk11

USER root

# 将代理破解包加入容器
COPY "atlassian-agent.jar" /opt/atlassian/jira/

# 设置启动加载代理包
RUN echo '\nexport JAVA_OPTS="-javaagent:/opt/atlassian/jira/atlassian-agent.jar ${JAVA_OPTS}"' >> /opt/atlassian/jira/bin/setenv.sh