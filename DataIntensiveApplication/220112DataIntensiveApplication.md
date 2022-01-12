# 차례

* Part1. 데이터 시스템의 기초
  * 신뢰성, 확장성, 유지보수성
  * 데이터 모델과 질의언어
  * 저장소와 검색
* Part2. 분산 데이터
  * 부호화
  * 복제
  * 파티셔닝
  * 트랜잭션
  * 분산 시스템에서 발생할 수 있는 문제
  * 일관성과 합의
* Part3. 파생 데이터
  * 일괄 처리
  * 스트림 처리
  * 데이터 시스템의 미래

# Part1. 데이터 시스템의 기초

* 결론 : 다양한 데이터 모델(문서, 관계형, 그래프)들을 보고 애플리케이션 요구사항에 가장 적합한 모델을 생각해보자. 선언형 질의 언어는 구현 부분과 분리가 가능하여 질의를 변경하지 않아도 성능향상이 가능하다.

* 데이터 모델과 질의언어

  * 데이터를 위한 질의 언어

    * 선언형, 명령형

    * 선언형

      * 결과가 충족해야 하는 조건, 데이터를 어떻게 변환해야하는지를 지정하면 목표를 달성해주는 질의 언어

    * 명령형

      * 특정 순서로 특정 연산을 수행하도록 컴퓨터에게 지시하는 질의 언어

    * 선언형 언어가 명령형 언어보다 좋은 점

      * 상세 구현이 숨겨져 있어 질의를 변경하지 않고도 시스템의 성능을 향상시킬 수 있다
      * 결과의 패턴만 지정하기 때문에 병렬 실행으로 더 빨라질 가능성이 크다

    * 선언형 언어 종류

      * SQL

        ```sql
        select * from animals where family = 'Sharks';
        ```

        

      * CSS

        * 선택된 제목들의 배경을 파란색으로 표시

        ```css
        li.selected > p {
            background-color: bule;
        }
        ```

        

      * XSL

        ```xsl
        <xsl:template match="li[@class='selected']/p">
        	<fo:block background-color="blue">
        		<xsl:apply-templates/>
        	</fo:block>
        </xsl:template>
        ```

        

    * 명령형 언어 종류

      * Javascript

        ```javascript
        function getSharks() {
            var sharks = [];
            for (var i = 0; i < animals.length; i++) {
                if (animals[i].family === "Sharks") {
                    sharks.push(animals[i]);
                }
            }
            return sharks;
        }
        ```

    * 맵리듀스 질의

      * 대량의 데이터를 처리하기 위한 프로그래밍 모델

      * 선언형과 명령형의 중간

      * map, reduce 함수를 기반으로 질의

      * map, reduce 모두 순수 함수이기 때문에 임의 순서로 어디서나 이 함수들을 실행할 수 있고 장애가 발생해도 재실행이 가능하다

      * 몽고DB의 경우 이러한 map reduce 모델을 사용하다가 함수 두개를 신중하게 작성하는 것이 어렵고, 선언형의 경우 질의 최적화기가 질의 성능을 높일 수 있다는 장점 때문에 2.2버전부터 집계 파이프라인(aggregation pipeline)이라는 선언형 질의 언어 지원을 추가했다

      * aggregation pipeline은 표현 측면에서 SQL의 부분 집합과 유사하다

      * mongoDB map reduce

        ```javascript
        db.observations.mapReduce(
        	function map() {
                var year = this.observationTimestamp.getFullYear();
                var month = this.observationTimestamp.getMonth() + 1;
                emit(year + "-" + month, this.numAnimals);
            },
            function reduce(key, values) {
                return Array.sum(values);
            },
            {
                query: { family: "Sharks" },
                out: "monthlySharkReport"
            }
        )
        ```

      * mongoDB aggregation pipeline

        ```javascript
        db.obsercations.aggregate([
            { $match: { family: "Sharks" } },
            { $group: {
                _id: {
                    year: { $year: "$observationTimestamp" },
                    month: { $month: "$obsercationTimestamp" }
                },
                totalAnimals: { $sum: "$numAnimals" }
            }}
        ]);
        ```

  * 그래프형 데이터 모델

    * 속성 그래프 모델 : Neo4j, Titan, InfiniteGraph

    * 트리플 저장소 모델(Triplestore, RDF store) : Datomic, Allegrograph

    * 속성 그래프

      * 정점

        * 고유한 식별자
        * 유출 간선 집합
        * 유입 간선 집합
        * 속성 컬렉션(키-값 쌍)
      * 간선
      
        * 고유한 식별자
          * 꼬리 정점
          * 머리 정점
          * 두 정점 간 관계 유형을 설명하는 레이블
          * 속성 컬렉션(키-값 쌍)
        * 정점과 정점은 간선으로 연결, 특정 유형과 관련 여부를 제한하는 스키마 없음
      * 일련의 정점을 따라 앞뒤 방향으로 순회한다(tail_vertex, head_vertex)
    
  * 사이퍼 질의 언어
    
    * 속성 그래프를 위한 선언형 질의 언어
      
      * neo4j 그래프 데이터베이스용
      
      * :WITHIN*0.. : 0회 이상 WITHIN간선을 따라가라
      
        ```cypher
        // 속성 그래프 표현
        CREATE
        	(NAmerica:Location {name:'North America', type:'continent'}),
        	(USA:Location {name:'United States', type:'country'}),
            (Idaho:Location {name:'Idaho', type:'state'}),
            (Lucy:Person {name:'Lucy'}),
            (Idaho) -[:WITHIN]-> (USA) -[:WITHIN]-> (NAmerica),
            (Lucy) -[:BORN_IN]-> (Idaho)
        // 미국에서 유럽으로 이민 온 사람 찾기
        MATCH
        	(person) -[:BORN_IN]-> () -[:WITHIN*0..]-> (us:Location {name:'United States'}),
          (person) -[:LIVES_IN]-> () -[:WITHIN*0..]-> (eu:Location {name:'Europe'})
        RETURN person.name
        ```
      
    * SQL 질의 언어
    
      * 관계형데이터베이스에서 속성 그래프를 표현하려면 가변적인 여러 간선을 순회해야 하고, 그러려면 조인 수를 고정할 수 없다
    * -[:WITHIN*0..]-> 와 같은 간선 순회를 WITH RECURSIVE로 표현할 수 있으나, 문법이 매우 어렵다
    
    ```sql
      --속성 그래프
    create table vertices (
      	vertex_id integer primary key,
    	properties json
      );
    
      create table edges (
      	edge_id integer primary key,
      	tail_vertex integer references vertices (vertex_id),
      	head_vertex integer references vertices (vertex_id),
      	label text,
      	properties json
      );
    
      create index edges_tails on edges (tail_vertex);
      create index edges_heads on edges (head_vertex);
      --미국에서 유럽으로 이민 온 사람 찾기
    ```
    
    * 트리플 저장소
    
      * 속성 그래프와 거의 동등하나 다른 용어를 사용해 설명
    
      * 주어, 서술어, 목적어로 저장(subject, predicate, object)
    
      * 트리플의 주어 = 속성 그래프의 정점
    
      * 정보 종류 (주어, 서술어, 목적어 순)
    
        * (루시, 나이, 33) : (정점, 속성의 키, 속성의 값)
        * (루시, 결혼하다, 알랭) : (정점, 간선, 정점)
    
      * Turtle로 표현
    
        * 기본적으로는 _:lucy a :Person. 과 같이 주어-서술어-목적어 로 표현
        * 코드와 같이 간결하게 표현도 가능
    
        ```turtle
        @prefix : <urn:example:>.
        
        _:lucy	a :Person;	:name "Lucy";	bornIn _:idaho.
        _:idaho	a :Location;	:name "Idaho";	:type "state";	:within _:usa.
        _:usa	a :Location;	:name "United States";	:type "country";	:within _:namerica.
        _:namerica	a :Location;	:name "North America";	:type "continent".
        ```
    
      * xml로 표현
    
        * RDF 모델(Resource Description Framework)
    
        * RDF 모델과 트리플의 차이점
    
          * RDF는 인터넷 전체의 데이터 교환을 위해 설계했기 때문에 서술어가 URI 일수도 있다
          * URI는 반드시 실제로 접속 가능한 주소일 필요는 없다
    
        * RDF가 등장한 배경
    
          * 웹 사이터의 데이터를 기계가 판독 가능한 데이터로도 정보를 게시하자는 개념이 나오고 시맨틱 웹을 만들자라는 배경에서 나옴
          * 인터넷을 만물 데이터베이스로
    
          ```xml
          <rdf:RDF xmlns="urn:example"
          	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
          	<Location rdf:nodeID="idaho">
              	<name>Idaho</name>
                  <type>state</type>
                  <within>
                  	<Location rdf:nodeID="usa">
                      	<name>United States</name>
                          <type>country</type>
                          <within>
                          	<Location rdf:nodeID:"namerica">
                              	<name>North America</name>
                                  <type>continent</type>
                              </Location>
                          </within>
                      </Location>
                  </within>
              </Location>
              
              <Person rdf:nodeID="lucy">
              	<name>Lucy</name>
                  <bornIn rdf:nodeID="idaho"/>
              </Person>
          </rdf:RDF>
          ```
    
    ​      
    
    * 스파클(SPARQL) 질의 언어
    
      * RDF 데이터 모델을 사용한 트리플 저장소 질의 언어
    
      * 사이퍼가 스파클을 차용했기 때문에 표현식이 유사하다
    
        ```SPARQL
        PREFIX : <urn:example:>
        
        SELECT ?personName WHERE {
            ?person :name ?personName.
            ?person :bornIn / :within* / :name "United States".
            ?person :liveIn / :within* / :name "Europe".
        }
        ```
    
    ​    
    
    * 데이터로그
    
      * 스파클, 사이퍼보다 오래된 언어(1980년대에 연구)
    
      * 데이토믹에서 사용
    
      * 캐스캘로그(Cascalog)는 데이터로그의 구현체로서 하둡의 대용량 데이터셋에 질의할 때 사용
    
      * 서술어(주어, 목적어) 형태로 작성
    
      * 다른 질의의 규칙을 결합하거나 재사용 가능
    
      * 일회성 질의 사용에는 편리하지 않지만 데이터가 복잡하면 효과적으로 대처 가능
    
        ```datalog
        /* 정의 */
        name(namerica, 'North America').
        type(namerica, continent).
        
        name(usa, 'United States').
        type(usa, country).
        within(usa, namerica).
        
        name(idaho, 'Idaho').
        type(idaho, state).
        within(idaho, usa).
        
        name(lucy, 'Lucy').
        born_in(lucy, idaho).
        /* 질의 */
        within_recursive(Location, Name) :- name(Location, Name).
        
        within_recursive(Location, Name) :- within(Location, Via),
        								within_recursive(Via, Name).
        								
        migrated(Name, BornIn, LivingIn) :- name(Person, Name),
        								born_in(Person, BornLoc),
        								within_recursive(BornLoc, BornIn),
        								lives_in(Person, LivingLoc),
        								within_recursive(LivingLoc, LivingIn).
        				
        ?- migrated(Who, 'United States', 'Europe').
        ```
    
    ​    
    
    * 그래프 모델과 네트워크 모델(코다실) 차이
    
      * 네트워크 모델은 다른 레코드 타입과 중첩 가능한 레코드 타입을 지정하는 스키마가 있지만, 그래프 모델은 없다
      * 네트워크 모델은 레코드의 접근 경로 중 하나를 탐색하는 방법으로만 특정 레코드에 도달가능하지만, 그래프 모델은 고유 ID를 가지고 직접 참조하거나 색인을 이용해 빠르게 정점을 찾을 수 있다
  
* 저장소와 검색