## Docker 설치

[Docker - official site](https://www.docker.com/products/docker-desktop)에서 Docker Desktop 설치

## M1 Mac유저는 

Rosetta2 필수적으로 설치해야함

```bash
softwareupdate --install-rosetta
```

## Docker version 확인

`docker -v` 

```bash
docker -v
Docker version 20.10.7, build f0df350
```

<img src="210721_05_Docker연결.assets/Screenshot 2021-07-21 at 1.00.39 PM.png" alt="Screenshot 2021-07-21 at 1.00.39 PM" style="zoom:30%;" />

## docker image 목록 확인 

`docker images`

<img src="210721_05_Docker연결.assets/Screenshot 2021-07-21 at 3.24.51 PM.png" alt="Screenshot 2021-07-21 at 3.24.51 PM" style="zoom:50%;" />

## docker container 목록 확인

`docker ps`

<img src="210721_05_Docker연결.assets/Screenshot 2021-07-21 at 3.26.03 PM.png" alt="Screenshot 2021-07-21 at 3.26.03 PM" style="zoom:50%;" />

## docker에서 neo4j 이미지 검색하기 

`docker search neo4j`

 <img src="210721_05_Docker연결.assets/Screenshot 2021-07-21 at 3.27.34 PM.png" alt="Screenshot 2021-07-21 at 3.27.34 PM" style="zoom:50%;" />

## Neo4j 이미지 pull

`docker pull neo4j`

<img src="210721_05_Docker연결.assets/Screenshot 2021-07-21 at 4.24.07 PM.png" style="zoom:50%;" />

## 오류 발생 

no matching manifest for linux/arm64/v8 in the manifest list entries 오류

* 아키텍처에 따라서 도커 이미지가 다르다
* 기존 intel CPU기반의 os는 linux/amd64 아키텍처 이미지를 사용
* 실리콘m1의 경우는 ARM64 사용 
* 즉, linux/arm64/v8 아키텍처의 이미지를 우선적으로 사용함.
* `--platform linux/arm64/v8`

* https://hub.docker.com/_/neo4j
  * Supported architectures: ([more info](https://github.com/docker-library/official-images#architectures-other-than-amd64)) [`amd64`](https://hub.docker.com/r/amd64/neo4j/)
  * linux/arm64/v8
* 그래서 앞에 Rosetta2를 통해 linux/amd64로 빌드된 어플도 실행 시켜야함

## neo4j 이미지 다시 pull 

```bash
docker pull --platform linux/amd64 neo4j


Using default tag: latest
latest: Pulling from library/neo4j
b4d181a07f80: Pull complete
3ee45ae97306: Pull complete
567d410fadc4: Pull complete
ad7fd4930617: Pull complete
d0619220af26: Pull complete
c0aede88a88b: Pull complete
3cfa6d382ecd: Pull complete
5c840d90d2dd: Pull complete
Digest: sha256:78c507172752737eb8e68f0877eb75172100f49f9f6a891829a002d1edc04779
Status: Downloaded newer image for neo4j:latest
docker.io/library/neo4j:latest
```

linux/amd64 이미지가 정상적으로 pull 



## 이미지 확인

`docker images`

 <img src="210721_05_Docker연결.assets/Screenshot 2021-07-21 at 5.06.37 PM.png" alt="Screenshot 2021-07-21 at 5.06.37 PM" style="zoom:50%;" />



## firstneo4j라는 container 생성 후 실행

```bash
docker run --platform linux/amd64 \
    --name firstneo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/1234 \
    neo4j:latest
```



<img src="210721_05_Docker연결.assets/Screenshot 2021-07-21 at 5.17.57 PM.png" alt="Screenshot 2021-07-21 at 5.17.57 PM" style="zoom:20%;" />

## Container 삭제

```bash 
docker rm firstneo4j
```



## Neo4j가 docker container에서 실행되는중인지 확인 

```bash
docker ps

CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                                                                            NAMES
e1917e9c9ab9   neo4j:latest   "/sbin/tini -g -- /d…"   25 seconds ago   Up 24 seconds   0.0.0.0:7474->7474/tcp, :::7474->7474/tcp, 7473/tcp, 0.0.0.0:7687->7687/tcp, :::7687->7687/tcp   firstneo4j
```

## Container 중지

```bash
docker stop firstneo4j
```

## Container 실행

```bash
docker start firstneo4j
```



```bash 
docker exec -it eloquent_swanson bash
```

```bash 
cypher-shell -u neo4j -p 1234
```



Connection refused 오류 

```bash
docker run --platform linux/amd64 --publish=7474:7474 --publish=7687:7687 -e 'NEO4J_AUTH=neo4j/1234' neo4j:latest
```





[다음시간]

* ARM64에서도 돌아가는 Neo4j이미지 찾아보기 (Neo4j가 아닌 다른 이름일수도)

* docker search 말고 docker hub에서 이미지 pull