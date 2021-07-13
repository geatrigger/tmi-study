FROM hadoop-base:3.3.1
# NameNode Web UI 응답 여부를 통해 Healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:9870/ || exit 1

WORKDIR /root
# 설정 파일 복제
ADD hdfs-site.xml ${HADOOP_HOME}/etc/hadoop/

# FsImage, EditLog 파일 경로를 volume으로 연결
RUN mkdir ${HADOOP_HOME}/dfs
RUN mkdir ${HADOOP_HOME}/dfs/name
VOLUME ${HADOOP_HOME}/dfs/name

# 실행 스크립트 복제
ADD start.sh /root/start.sh
RUN chmod a+x /root/start.sh

# NameNode의 HTTP, IPC 포트 노출
EXPOSE 9870 9000

# 시작 명령어 등록
CMD ["/root/start.sh", "${HADOOP_HOME}/dfs/name"]