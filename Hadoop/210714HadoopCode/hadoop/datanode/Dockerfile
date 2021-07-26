FROM hadoop-base:3.3.1

# DataNode Web UI 응답 여부를 통해 Healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3  CMD curl -f http://localhost:9864/ || exit 1

ADD hdfs-site.xml ${HADOOP_HOME}/etc/hadoop/
RUN mkdir ${HADOOP_HOME}/dfs
RUN mkdir ${HADOOP_HOME}/dfs/data
VOLUME ${HADOOP_HOME}/dfs/data

ADD start.sh /root/start.sh
RUN chmod a+x /root/start.sh

# WebUI, 데이터전송
EXPOSE 9864 9866

CMD ["/root/start.sh"]