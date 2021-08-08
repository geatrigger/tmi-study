Neo4j 내부 GraphApps 소개 

#### 데이터 설명

* 여러 나라의 맥주와 맥주공장에 대한 데이터
* https://openbeerdb.com/

```cypher
CALL db.schema.visualization()
```

![graph](210807_08_Neo4jBloom.assets/graph-8387185.png)

## Neo4j Bloom

* visualisation을 위한 앱

* 다만, 엄청 큰 Graph의 가시화는 지원하지 않음

  * 아주 큰 Node들의 전체 모습을 보기에는 적절치 않음
  * 작은 network에서 직관적인 관계를 보기에 적합 

* Cyper 지원하지 않음

* 주요 기능

  <img src="210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 12.32.42 PM.png" alt="Screenshot 2021-08-08 at 12.32.42 PM" style="zoom:50%;" />

  <img src="210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 12.33.41 PM.png" alt="Screenshot 2021-08-08 at 12.33.41 PM" style="zoom:50%;" />

  `Brewery of Pumpkin Ale`

  

  <img src="210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 12.36.50 PM.png" alt="Screenshot 2021-08-08 at 12.36.50 PM" style="zoom:50%;" />

  `Beer of Brewery of Pumpkin Ale`

  <img src="210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 12.38.35 PM.png" alt="Screenshot 2021-08-08 at 12.38.35 PM" style="zoom:50%;" />

  

  

  * Search phrases 

  ```cypher
  MATCH (n1:Beer),(n2:Beer)
  WHERE n1.name = $beer1 and n2.name = $beer2
  WITH n1,n2
  MATCH path = allshortestpaths((n1)-[*]-(n2))
  RETURN path
  ```

  `beer1 21A IPA and beer2 Porter`

  ![Screenshot 2021-08-08 at 12.53.36 PM](210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 12.53.36 PM.png)

  ```cypher
  MATCH r=(c:Category)<-[:BEER_CATEGORY]-(b:Beer)-[:BREWED_AT]->(br:Brewery) WHERE
        br.country = $b1 AND
       c.category = $c1
  RETURN r
  ```

  ![Screenshot 2021-08-08 at 10.59.37 AM](210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 10.59.37 AM.png)

  * rule-based styling

    * ABV (alcohol by volume) > 8.0 

    ![Screenshot 2021-08-08 at 11.14.46 AM](210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 11.14.46 AM.png)

## Neo4j Dash

* 2020년 11월 첫 출시
* 2021년 6월 NeoDash 1.1 출시
* Neo4j 데이터베이스를 dashboard스타일로 
* 지원 형식 : Table, Graph, Line Chart, Bar Chart, Selection ...etc

Type : Selection Box를 이용하여 Cyper parameters를 쉽게 설정 

```cypher
MATCH (c:Category)<-[:BEER_CATEGORY]-(b:Beer)-[:BREWED_AT]->(br:Brewery) WHERE
      br.country = $neodash_brewery_country AND
     c.category = $neodash_category_category
RETURN b.name as Beer, br.name as Brewery
```



Type : Map Box를 이용하여 지도 시각화 

* Node의 Property에 위도 경도가 있다면 자동으로 선택해 지도 생성

![Screenshot 2021-08-08 at 11.33.35 AM](210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 11.33.35 AM.png)

Type : Line chart

```cypher
MATCH (br:Brewery) 
WITH br.country as country 
WITH DISTINCT country, 
COUNT(country)as num_coun 
RETURN *
```

<img src="210807_08_Neo4jBloom.assets/Screenshot 2021-08-08 at 12.22.47 PM.png" alt="Screenshot 2021-08-08 at 12.22.47 PM" style="zoom:50%;" />

