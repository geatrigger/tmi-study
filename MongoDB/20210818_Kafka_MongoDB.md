### kafka in docker container

![topic](https://miro.medium.com/max/994/1*ipMuwhEg-LO6wBCy1jlkpg.png)



작업공간 생성 및 이동

```bash
mkdir kafka-mongo
cd kafka-mongo
```



zookeeper, kafka 컨테이너 실행을 위한 docker-compose.yaml 작성

kafka 환경변수

- `KAFKA_ADVERTISED_LISTENERS` : kafka 브로커를 가리키는 사용 가능 주소 목록. kafka는 초기 연결 시 이를 client에게 보냄
- `KAFKA_LISTENERS` : kafka 브로커가 들어오는 연결을 수신 대기하는 주소 및 리스너 이름 목록
- `KAFKA_ZOOKEEPER_CONNECT` : ZooKeeper 연결 문자열. ,로 구분 ex) <zookeeper서버의 hostname>:<zookeeper서버의 포트번호>
- `KAFKA_CREATE_TOPICS` : 생성할 Topic명:Partition 개수:Replica 개수

```yaml
version: '2'

networks:
  test:

services:
  zookeeper:
    image: wurstmeister/zookeeper:3.4.6
    container_name: zookeeper
    ports:
      - "2181:2181"
    networks:
      - test

  kafka:
    image: wurstmeister/kafka:2.12-2.0.1
    container_name: kafka
    environment:
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      KAFKA_ADVERTISED_HOST_NAME: 127.0.0.1
      KAFKA_ADVERTISED_PORT: 9092
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_CREATE_TOPICS: "javainuse-topic:1:1"   # Topic명:Partition개수:Replica개수
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - "9092:9092"
    depends_on:
      - zookeeper
    networks:
      - test
```



zookeeper, kafka 컨테이너 실행

```bash
docker-compose up -d
```



새 콘솔에서 kafka 바이너리 파일 다운로드(F12눌러서 파일주소 가져옴)

kafka가 제대로 실행되었는지 확인하기 위해 공식 사이트에서 kafka 바이너리 파일을 docker-compose에서 설정한 kafka버전과 맞춰서 다운로드

이를 위해 kafka 컨테이너 이미지 버전을 ``latest``가 아닌 고정된 버전으로 사용 추천

```bash
cd kafka-mongo
wget https://archive.apache.org/dist/kafka/2.0.1/kafka_2.12-2.0.1.tgz
tar -xvzf kafka_2.12-2.0.1.tgz
rm kafka_2.12-2.0.1.tgz
```



kafka topic 생성 확인

새 콘솔에서 kafka 컨테이너에서 설정한  '`javainuse-topic`' topic이 제대로 생성되었는지 확인

`bin/kafka-topics.sh` 실행 옵션

- --zookeeper : zookeeper가 실행 중인 호스트. 별도의 서버에 구축했다면 `server_ip:server_port`로 지정
- --list : 리스트 출력
- --create : topic 생성
- --topic : 생성할 topic명
- --partitions : 생성할 topic의 파티션 개수
- --replication-factor : 생성할 topic의 복사본 개수

```bash
cd kafka-mongo/kafka_2.12-2.0.1
sh bin/kafka-topics.sh --zookeeper localhost:2181 --list
```



새 콘솔에서 **kafka Consumer** 실행해 메세지 수신 상태로 대기시킴

`bin/kafka-console-consumer.sh` 실행 옵션

- --topic : 메시지를 가져올 topic. 여기에선 kafka 컨테이너 실행 시에 생성한 `javainuse-topic`으로 설정
- --bootstrap-server : kafka가 실행 중인 호스트. 별도의 서버에 구축했다면 `server_ip:server_port`로 지정
- --from-beginning : 맨 처음부터 메시지를 가져옴

```bash 
cd kafka-mongo/kafka_2.12-2.0.1
bin/kafka-console-consumer.sh --topic javainuse-topic --bootstrap-server localhost:9092 --from-beginning
```



새 콘솔에서 **kafka Producer** 실행해 메세지 생산 상태로 대기시킴

``>`` 이 출력되면서 입력 대기 상태가 됨

`bin/kafka-console-producer.sh` 실행 옵션

- --topic : 메시지를 생산할 topic. 여기에선 kafka 컨테이너 실행 시에 생성한 `javainuse-topic`으로 설정
- --broker-list : kafka가 실행 중인 호스트. 별도의 서버에 구축했다면 `server_ip:server_port`로 지정

kafka 메세지 전송

Producer에서 console에 메시지를 입력한 뒤 ``Enter``를 누르면 Consumer를 실행한 console에 생산한 메세지 출력됨

```bash
cd kafka-mongo/kafka_2.12-2.0.1
bin/kafka-console-producer.sh --topic javainuse-topic --broker-list localhost:9092
```





#### connector 필요

docker  mongodb image 다운

```bash
docker pull mongo
```

mongodb container 생성

```bash
docker run -d --name mongo-db -v /data:/data/db -p 27017:27017 mongo:4.2
```

mongodb container에 접속

```bash
docker exec -it mongo-db /bin/bash
```

컨테이너 내부에서 mongodb 접속

mongodb 종료 : ctrl+c  

컨테이너 빠져나오기 : exit 입력

```bash
mongo
```





### Kafka, MongoDB, 파이썬 기반 메시지 스트리밍 

Producer, Consumer in Python

ubuntu에서 pip명령어로 라이브러리 설치를 위해 pip설치

```bash
sudo apt install python3-pip
pip --version
```

```bash
pip install kafka-python
```

```bash
pip install pymongo
```



**kafka_server.py** 파이썬 파일 생성

```python
from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(5000):
    print("Iteration", e)
    data = {'number' : e}
    producer.send('numtest', value=data)
    sleep(1)
```

```bash
cd MongoDB/kafka-mongo
python3 kafka_server.py
```



**kafka_consumer.py** 파이썬 파일 생성

```bash
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.numtest.numtest
     
for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))
```

```bash
python3 kafka_consumer.py 
```



MnogoDB 에 연결하면 kafka에서 생성된 데이터가 저장된것을 확인가능

```bash
mongo

use admin

db.createUser({user:'statice', pwd:'1008', roles:['root'],mechanisms : ["SCRAM-SHA-1"]})
```



```bash
use numtest

show collections

db.numtest.find()
```



- Ubuntu MongoDB - MongoDB compass 연결

- python거쳐서 producer 속도 issue

  카프카에서 몽고디비로 바로 연결

  connector 알아보기







