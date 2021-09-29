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

* 