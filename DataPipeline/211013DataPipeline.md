# 지난 내용들 요약

* 설치프로그램

  * 모든 서버 ubuntu 18.04 LTS

  * 서버별 구성요소들

    ![210920SmartCarLog](210927DataPipeline.assets/210920SmartCarLog.png)

* 계획

  * Hadoop, YARN, HBase와 같이 공통으로 설치된 요소들은 한 서버에 설치후 복제하여 환경을 갖춘다
  * 그 외의 요소들은 책에 쓰인 순서대로 설치하고 테스트해본다
  * 프로그램 중 오픈소스가 아닌 프로그램들은 검색하여 대체 or 생략한다

* 파이프라인 구조

  * cloudera manager는 제외

  ![h9nelLcaQ9OB3CQGMLTHbPFNmOggwj9V](211013DataPipeline.assets/h9nelLcaQ9OB3CQGMLTHbPFNmOggwj9V.jpg)

* 현재 상황

  * server 사전작업
    * ubuntu 18.04 LTS 설치
    * java 8버전 설치
  * Hadoop, YARN 설치
    * server ip주소, 주변 호스트 정보 설정
    * server끼리 ssh통신 설정
    * Hadoop, YARN xml파일 설정
    * Hadoop, YARN 실행
  * Zookeeper 설치 <------------------------------------ 다음 순서
  * 스마트카 로그 시뮬레이터 설치
  * Flume 설치
  * Kafka 설치
  * 수집 기능 테스트
    * Flume -> Kafka
  * HBase 설치
  * Redis 설치
  * Storm 설치
  * Esper 설치
  * 적재 기능 테스트
    * Flume -> HDFS
    * 실시간 적재
      * Flume -> Kafka -> Storm -> Redis
      * Flume -> Kafka -> Storm -> HBase
  * Hive 설치
  * Spark 설치
  * Oozie 설치
  * Hue 설치
  * 탐색 기능 테스트
  * Impala 설치
  * Zeppelin 설치
  * Mahout 설치
  * Sqoop 설치
    * MySQL 설치(PostgreSQL 대신)

# Zookeeper 설치

* Server02

* zookeeper 역할

  * https://zookeeper.apache.org/doc/r3.6.3/zookeeperOver.html
  * https://oboki.net/workspace/data-engineering/zookeeper/zookeeper-3-x-%EC%84%A4%EC%B9%98/
  * a distributed, open-source coordination service for distributed applications
  * 분산 시스템 간의 정보를 공유, 서버들의 상태 체크, 동기화를 위한 lock처리
  * coordination service
  * 데이타 접근이 빠르고, 장애에 대한 대응성을 가져야 한다
  * 디렉토리 구조기반으로 znode라는 데이터 저장 객체 제공(key-value), 생성 및 삭제 가능

* zookeeper 계정 생성

  * 따로 관리하기 위해 생성

  * root로 접속(비번 : adminuser)

    ```shell
    sudo groupadd -g 20000 zookeeper
    sudo useradd -g zookeeper -u 20000 -m zkuser # m옵션 없으면 디렉토리 생성안함
    sudo passwd zkuser # 비밀번호 : zkuser
    # group확인은 /etc/group에서
    # user확인은 /etc/passwd에서
    # 기본 쉘 /bin/bash로 변경
    chsh
    ```

  * /etc/sudoers를 이용해 zkuser sudo 권한 부여

    ```shell
    zkuser ALL=(ALL) NOPASSWD: ALL
    ```

    

* zookeeper 다운 및 압축풀기

  * 현시점 latest stable 버전다운

  * http://zookeeper.apache.org/releases.html

    ```shell
    wget https://dlcdn.apache.org/zookeeper/zookeeper-3.6.3/apache-zookeeper-3.6.3-bin.tar.gz
    
    # /usr/local/에 압축풀기
    sudo tar xvzf apache-zookeeper-3.6.3-bin.tar.gz -C /usr/local/
    # 사용자와 그룹 지정
    sudo chown -R zkuser:zookeeper /usr/local/apache-zookeeper-3.6.3-bin/
    ```

* bashrc에 환경변수설정

  ```shell
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
  export ZOOKEEPER_HOME=/usr/local/apache-zookeeper-3.6.3-bin
  export PATH=$PATH:$JAVA_HOME/bin:$ZOOKEEPER_HOME/bin
  ```

* conf/zoo.cfg 생성

  * zoo_sample.cfg를 복사하여 값 수정

  * https://zookeeper.apache.org/doc/r3.6.3/zookeeperStarted.html

  * production 에선 replicated mode로 사용하고, 그럴 경우 옵션을 더 적어줘야 한다

    ```shell
    # The number of milliseconds of each tick
    tickTime=2000
    # The number of ticks that the initial
    # synchronization phase can take
    initLimit=10
    # The number of ticks that can pass between
    # sending a request and getting an acknowledgement
    syncLimit=5
    # the directory where the snapshot is stored.
    # do not use /tmp for storage, /tmp here is just
    # example sakes.
    dataDir=/data/zookeeper
    # the port at which the clients will connect
    clientPort=2181
    
    # replicated mode
    # server.1=server01:2888:3888
    # server.2=server02:2888:3888
    # server.3=server03:2888:3888
    ```

* zookeeper 실행

  * https://oboki.net/workspace/data-engineering/zookeeper/zookeeper-3-x-%EC%84%A4%EC%B9%98/
  * replicated mode에선 Mode가 follwer 혹은 leader로 설정되어 있다

  ```shell
  zkServer.sh start
  zkServer.sh status
  ```

  ![image-20210929174729145](211013DataPipeline.assets/image-20210929174729145.png)

* zookeeper 연결

  ```shell
  zkCli.sh -server 127.0.0.1:2181
  # 테스트
  create /pilot-pjt bigdata
  ls /
  get /pilot-pjt
  delete /pilot-pjt
  ```

  ![image-20210929200410426](211013DataPipeline.assets/image-20210929200410426.png)

* systemmd

  * https://twofootdog.tistory.com/89

  * systemmd 에 등록함으로써 리눅스에서 여러 프로세스를 효율적으로 관리할 수 있게 된다

  * 일단 스킵

    ```shell
    # /etc/systemd/system/zookeeper-server.service 서비스파일 생성
    [Unit]
    Description=zookeeper-server
    After=network.target
    
    [Service]
    Type=forking
    User=root
    Group=root
    SyslogIdentifier=zookeeper-server
    WorkingDirectory=/usr/local/zookeeper
    Restart=always
    RestartSec=0s
    ExecStart=/usr/local/zookeeper/bin/zkServer.sh start
    ExecStop=/usr/local/zookeeper/bin/zkServer.sh stop
    ```

  * systemd 리로드 및 systemctl 시작

    ```shell
    systemctl daemon-reload
    # 기존에 실행되는 zkServer.sh의 프로세스가 없어야 함
    systemctl start zookeeper-server
    ```

    

# 스마트카 로그 시뮬레이터 설치

* Server02

* 로그 폴더 생성 및 권한 부여

  ```shell
  mkdir /home/pilot-pjt/working/car-batch-log -p
  mkdir /home/pilot-pjt/working/driver-realtime-log -p
  chmod 777 -R /home/pilot-pjt/
  ```

* bigdata.smartcar.loggen-1.0.jar 파일을 /home/pilot-pjt/working에 옮기기

  * https://github.com/wikibook/bigdata2nd
  * ch2 폴더

* 로그 시뮬레이터 실행

  ```shell
  # DriverLogMain.java
  # 1번창
  java -cp bigdata.smartcar.loggen-1.0.jar com.wikibook.bigdata.smartcar.loggen.DriverLogMain 20160101 10
  # 2번창
  tail -f SmartCarDriverInfo.log
  
  # CarLogMain.java
  # 1번창
  java -cp bigdata.smartcar.loggen-1.0.jar com.wikibook.bigdata.smartcar.loggen.CarLogMain 20160101 10
  # 2번창
  tail -f SmartCarStatusInfo_20160101.txt
  ```

  ![image-20210929205128407](211013DataPipeline.assets/image-20210929205128407.png)