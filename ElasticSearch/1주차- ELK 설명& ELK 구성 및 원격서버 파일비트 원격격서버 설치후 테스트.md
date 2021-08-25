# 1주차- ELK 설명& ELK 구성 및 원격서버 파일비트 설치후 테스트

### ELK-Stack 이란

"ELK"는 Elasticsearch, Logstash 및 Kibana, 이 오픈 소스 프로젝트 세 개의 머리글

Elasticsearch는 검색 및 분석 엔진. JSON 기반의 분산형 오픈 소스 RESTful 검색 엔진으로, 사용하기 쉽고, 확장 가능하며, 유연하여 검색 분야에서는 사용자와 회사의 팬덤과 높은 인기를 누림

 Logstash는 여러 소스에서 동시에 데이터를 수집하여 변환한 후 Elasticsearch 같은 “stash”로 전송하는 서버 사이드 데이터 처리 파이프라인

 Kibana는 사용자가 Elasticsearch에서 차트와 그래프를 이용해 데이터를 시각화할 수 있게 해줌

Beats 는 이후 2015년에, ELK Stack에 경량의 단일 목적 데이터 수집기 제품군을 도입되었음

### ELK stack 구조

Elk stack 의 기본적인 구조는 다음과 같다.


![ELK stack 기본 구조](./images/ELK%20Stack%20기본%20구조.png)

하지만 경우에 따라, 대량의 데이터를 처리하기 위해 구축된 더 복잡한 파이프라인을 처리하기 위해 복원력(Kafka, RabbitMQ, Redis) 및 보안(nginx)을 위해 추가 구성 요소가 로깅 아키텍처에 추가될 가능성이 있음


![ELK Stack 확장](./images/ELK%20Stack%20확장.png)

### You know, for Search

강력한 검색기능과 분산처리 그리고 개발과 소통이 활발한 커뮤니티 덕에 지금은 검색엔진 분야에서 지배적인 위치에 있음.

![검색엔진 순위](./images/검색엔진%20순위%20.png)


### 환경구성 : docker 이용

docker 에 설치하기전 사전 설정

sudo vi /etc/sysctl.conf

vm.max_map_count=262144 입력

sudo sysctl -p 로 적용

docker-compose.yml

1번 서버에 ,**elasticsearch cluster 구성 , kibana link**

```yaml
version: '2.2'
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.14.0
    container_name: es01
    environment:
      - node.name=es01
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es02,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - elastic

  es02:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.14.0
    container_name: es02
    environment:
      - node.name=es02
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es01,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data02:/usr/share/elasticsearch/data
    networks:
      - elastic

  es03:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.14.0
    container_name: es03
    environment:
      - node.name=es03
      - cluster.name=es-docker-cluster
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data03:/usr/share/elasticsearch/data
    networks:
      - elastic

  kib01:
    image: docker.elastic.co/kibana/kibana:7.14.0
    container_name: kib01
    ports:
      - 5601:5601
    environment:
      ELASTICSEARCH_URL: http://es01:9200
      ELASTICSEARCH_HOSTS: '["http://es01:9200","http://es02:9200","http://es03:9200"]'
    networks:
      - elastic

volumes:
  data01:
    driver: local
  data02:
    driver: local
  data03:
    driver: local

networks:
  elastic:
    driver: bridge
```

2번서버에 filebeat 설치 및 elasticsearch 연동

filebeat.yml

```yaml
filebeat.inputs:
- type: log

  # Change to true to enable this input configuration.
  enabled: true

  # Paths that should be crawled and fetched. Glob based paths.
  paths:
    - /var/log/sample_filebeat.log
:
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["spark-hsjang--1:9200"]
```

샘플데이터에 데이터 저장할때마다 엘라스틱서치에 바로 업로드 되는게 확인됨
