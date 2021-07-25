# Hadoop 3.3.1의 전체 특징

* https://hadoop.apache.org/docs/r3.3.1/index.html

* HDFS에서 erasure coding 지원

  * https://joonyon.tistory.com/67

  * 기존 장애허용성을 위해 replication으로 3x의 overhead가 들었는데, erasure coding을 사용하면 1.5x의 overhead만으로 똑같은 수준의 장애허용성을 가지게 할 수 있다(기본 EC policy인 RS(6, 3) 기준, 6개의 data block과 3개의 parity block)

  * decode하는 과정이 필요하기 때문에 replication하는 것보다는 읽기가 느리다

  * 일부 실행불가능한 HDFS operation들이 생긴다

    * hflush, hsync, concat, setReplication, truncate, append

  * policy들의 명명방법

    * *codec*-*num data blocks*-*num parity blocks*-*cell size*
    * built-in policies : RS-3-2-1024k, RS-6-3-1024k, RS-10-4-1024k, RS-LEGACY-6-3-1024k, XOR-2-1-1024k
    * intel의 경우 자체적으로 제공하는 ISA-L이 있어서 RS, XOR codec을 실행할 때 더 나은 퍼포먼스를 보여준다(RS-LEGACY는 불가능). intel이 아닌 다른 프로세서에서 실행할 때는 pure Java로 실행해야만 한다

  * ec 세팅하는 법

    * 기본적으로 erasure coding policies는 disabled
    * node-level fault-tolerance를 지키기 위해서 해당 ec policy에 대해 data block수+parity block수보다 data node가 많은지 확인(ex RS-6-3-1024k의 경우 6+3=9)
    * rack fault-tolerance를 지키고 싶다면, 해당 ec policy에 대해 (data blocks + parity blocks) / parity blocks개 이상의 rack이 있는지 확인(ex RS-6-3-1024k의 경우 (6+3)/3=3)
    * policy지정

    ```shell
    # 디폴트 policy지정
    hdfs ec -enablePolicy -policy <policyName>
    # 특정 디렉토리에 policy지정
    hdfs ec -setPolicy -path <path> [-policy <policyName>] [-replicate]
    # 특정 디렉토리의 policy파악하기
    hdfs ec -getPolicy -path <path>
    ```

* Shaded client jars

  * 기존 2버전에서 Hadoop transitive dependency들이 Hadoop application’s classpath에 새어나가는 것을 막았다
  
* 그 외

  * Java 버전 최소사항이 Java7에서 Java8로 증가
  * YARN Timeline Service v2(alpha버전) 제공
    * Timeline의 scalability와 reliability 상승, flow와 aggregation을 소개하여 사용성 향상
  * 기존에 있던 버그있는 shell sript 대폭 수정
  * Support for Opportunistic Containers and Distributed Scheduling
  * MapReduce의 task level에서의 최적화
  * Support for more than 2 NameNodes
  * 기본 포트번호 변화
    * 기존 하둡 서비스들의 기본포트가 Linux ephemeral port range(32768-61000)에 있어서 종종 서비스가 다른 어플리케이션과의 충돌로 인해 port binding에 실패하여 다른 포트번호로 바꿈
  * Microsoft Azure Data Lake와 Aliyun Object Storage System와 같은 filesystem과 통합 가능
  * Intra-datanode balancer
    * 기존에는 add, replace작업을 하면 intra-datanode(하나의 데이터 노드 내에서)단계에서 skew가 일어남
    * hdfs diskbalancer를 통해 intra-datanode balacer를 실행시킬 수 있게 됨
  * Reworked daemon and task heap management
  * S3Guard: Consistency and Metadata Caching for the S3A filesystem client
  * HDFS Router-Based Federation
  * API-based configuration of Capacity Scheduler queue configuration
  * YARN Resource Types

# Single node setup

* 의존성 설치

  * Java
  * ssh
  * pdsh(필수는 아님)

* Dockerfile에 환경변수 등록

  ```dockerfile
  # 기존에 있던 환경변수
  ENV HADOOP_HOME /root/hadoop
  # 새로 등록한 환경변수
  # PATH 업데이트하여 ${HADOOP_HOME}/bin를 입력안해도 hdfs, hadoop을 실행가능하게 함
  # {}안넣으면 인식 안됨
  ENV HADOOP_CLASSPATH="${JAVA_HOME}/lib/tools.jar"
  ENV PATH="${HADOOP_HOME}/bin:${PATH}"
  ```

* grep example

  ```shell
  hdfs dfs -rm -R /output
  hdfs dfs -mkdir /input
  # input으로 들어갈 파일들
  hdfs dfs -copyFromLocal $HADOOP_HOME/etc/hadoop/*.xml /input
  # input, output은 반드시 /input, /output이라 써야함
  hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar grep /input /output 'dfs[a-z.]+'
  # 내용파악
  hdfs dfs -cat /output/part-r-00000 | head -10
  ```

# Cluster setup

* https://hadoop.apache.org/docs/r3.3.1/hadoop-project-dist/hadoop-common/ClusterSetup.html
* 설치시 참고사항
  * 모든 machine에 hadoop software가 설치되어야 한다
  * 주로 NameNode, ResourceManager는 다른 machine위에서 돌아가고 이를 통틀어 masters라고 부른다
  * 그 외의 다른 서비스들(Web App Proxy Server, MapReduce Job History Server등)은 전용 하드웨어나 공용 하드웨어 위에서 사용한다
  * DataNode와 NodeManager는 workers라고 부른다

* 하둡 daemon의 환경설정

  * 뼈대만 있는 쉘 스크립트 용도에 맞게 수정하여 사용

  * etc/hadoop/hadoop-env

    | NameNode                      | HDFS_NAMENODE_OPTS          |
    | ----------------------------- | --------------------------- |
    | DataNode                      | HDFS_DATANODE_OPTS          |
    | Secondary NameNode            | HDFS_SECONDARYNAMENODE_OPTS |
    | ResourceManager               | YARN_RESOURCEMANAGER_OPTS   |
    | NodeManager                   | YARN_NODEMANAGER_OPTS       |
    | WebAppProxy                   | YARN_PROXYSERVER_OPTS       |
    | Map Reduce Job History Server | MAPRED_HISTORYSERVER_OPTS   |

  * etc/hadoop/mapred-env.sh

  * etc/hadoop/yarn-env.sh

* 하둡 daemon의 설정

  * etc/hadoop/core-site.xml
    * fs.defaultFS
    * io.file.buffer.size
  * etc/hadoop/hdfs-site.xml

