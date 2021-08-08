# tmi 스터디

* 0주차(2021-06-16)
  * 스터디 방향성 회의
* 1주차(2021-06-23)
  * 발표 주제
    * 김기찬 : 도커 사용이유와 사용방법
    * 김예지 : 다양한 데이터에 따른 효과적인 표현방법
    * 최진영 : 빅데이터 이용된 마케팅 사례
  * 전체적인 데이터 엔지니어/사이언티스트 흐름을 파악하기로 함
    * 다음 주제는 데이터 엔지니어 로드맵 전체 흐름 발표
* 2주차(2021-06-30)
  * 발표 주제
    * 김기찬 : 데이터 엔지니어 로드맵 전체 흐름
    * 김예지 : 데이터 엔지니어 로드맵 중 커맨드라인, api
    * 최진영 : 현직 데이터 엔지니어 하는 일 스크랩, 데이터 엔지니어 로드맵 중 encryption
  * 전체적인 흐름을 보기에는 배경지식이 너무 많이 필요하여 세부적인 내용 하나씩 조사하기로 함
* 3주차(2021-07-07)
  * 발표 주제
    * 김기찬 : Docker-compose를 사용해서 MySQL, python 연동 시켜서 실제로 사용하는 법
    * 김예지 : Neo4j 사용법
* 4주차(2021-07-14)
  * 발표 주제
    * 김기찬 : Hadoop 설치 및 HDFS실행
    * 김예지 : neo4j 예제 돌려서 장점 확인해보기
  * 새로운 멤버 합류
* 5주차(2021-07-21)
  * 발표 주제
    * 김기찬 : Hadoop Map Reduce
    * 김예지 : neo4j를 docker로 돌려보기
    * 김현용 : Mongo 쓰는 방법
* 6주차(2021-07-28)
  * 발표 주제
    * 김기찬 : Hadoop 3.3.1의 새로운 특징과 Hadoop세팅변수설정, HDFS의 목표점과 NameNode, DataNode의 역할
    * 김예지 : 추천시스템(협업필터링과 콘텐츠 기반 필터링정리).Neo4j와 Cyper를 사용해 콘텐츠 기반 필터링 영화 추천 모델 예제수행
      * Content-based filtering 모델을 간단하게 만들어보았고 Neo4j의 장점인 노드와 노드 사이의 연결을 그래프로 직관적이게 시각화 수행함. 
      * 다른 Nosql과 비교했을 때는 아직까지는 시각화의 장점만 보임.
    * 김현용 : RDBMS와 비교한 MongoDB의 기본개념 정리.  MongoDB 환경설정 및 CRUD 데이터핸들링
* 7주차(2021-08-04)
  * 발표 주제
    * 김예지 : style.grass이용해 그래프 스타일 설정 변경/ Similarity Metrics(Cosine,Pearson similarity)을 이용한 쿼리문으로 추천영화 예제
    * 김기찬 : kafka와 spark의 차이, kafka 실행 예제
    * 김현용 : docker container를 이용한 MongoDB 샤딩 환경 세팅
  * 새로운 멤버 합류
  * 발표시간은 20분으로 줄이기
* 8주차(2021-08-08)
  * 발표 주제
    * 김예지 : Neo4j 내부 graph application인 Neo4j Bloom과 Neo4j Dash 소개
    * 김기찬 : kafka cluster 구축 및 기능 테스트
    * 김현용 : ip주소, port번호, protocol 기본 정리
    * 장현석 : ELK 설명& ELK 구성 및 원격서버 파일비트 설치후 테스트

# 스터디 진행 방향

* 조사할 데이터 및 개발 관련된 주제를 각자 정하고 글을 남겨서 적절한 주제인지 서로 검토한다
  * 데이터 엔지니어 로드맵, 데이터 사이언티스트 로드맵에 있는 것과 무조건 연관시켜서
* 1주정도 기간동안 조사하고 정리한다
* 발표자료(마크다운)와 코드등을 올린다
* 한 사람당 10분~20분을 가진다
* 반복

# 스터디 규칙

* 모이는 날 참여 불가능하면 미리 말하기(단, 경조사 등이 아니라 단순히 준비하기 싫어서는 안됨)
  * 인원이 적으면 날짜를 아예 바꾸기
* 무단으로 불참하면 스터디 제외
* 자료(발표자료, 정리자료, 코드 등)는 발표전에 깃에 올리기
  * 주제
  * 딥러닝>210616자연어처리.md
* 발표자료는 markdown
* 질의응답 때 시간이 너무 오래걸리거나 중요도가 낮은 질문에 대해선 발표자 재량으로 넘어갈 수 있다.
* 발표주제는 단순히 수업내용을 복습하는 것은 안된다(새로운 것이어야 함)
* 발표가 끝나고 나서 각자 발표한 주제를 각자 정리해서 보내주기
* 각자 발표가 끝난 후 Q&A 질문이나 피드백 하나 이상 하기
* git convention 통일
  * 날짜 | 한글로 명확한 제목
  * 210728 | 6번째 회의록