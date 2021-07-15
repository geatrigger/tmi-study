# Neo4j 기초3(with 예제데이터)

### 기존 데이터 지우기

```cypher
MATCH (n) DETACH DELETE n
```



### 노드 & 관계 만들기

```cypher
CREATE (alice:Person {name:"Alice"})-[:IS_FRIEND_OF]->(judy:Person {name:"Judy"}),
       (alice)-[:IS_FRIEND_OF]->(sayaka:Person {name:"Sayaka"}),
       (alice)-[:IS_FRIEND_OF]->(kimlee:Person {name:"Kim Lee"}),
       (alice)-[:IS_FRIEND_OF]->(emily:Person {name:"Emily"}),
       (alice)-[:IS_FRIEND_OF]->(daisy:Person {name:"Daisy"}),
       (alice)-[:IS_FRIEND_OF]->(nguyenhanh:Person {name:"Nguyen Hanh"}),
       (alice)-[:IS_FRIEND_OF]->(liting:Person {name:"Li Ting"}),
       (jurongeast:Location {name:"Jurong East"}),
       (jurongwest:Location {name:"Jurong West"}),
       (jurongnorth:Location {name:"Jurong North"}),
       (jurongsouth:Location {name:"Jurong South"}),
       (japanese:Cuisine {name:"Japanese"}),
       (chinese:Cuisine {name:"Chinese"}),
       (korean:Cuisine {name:"Korean"}),
       (thai:Cuisine {name:"Thai"}),
       (vietnamese:Cuisine {name:"Vietnamese"}),
       (koreanbbq:Restaurant {name:"Korean BBQ"})-[:SERVES]->(korean),(koreanbbq)-[:LOCATED_IN]->(jurongeast),
       (kimlee)-[:LIKES]->(koreanbbq),
       (judy)-[:LIKES]->(koreanbbq),
       (zensushi:Restaurant {name:"Zen Sushi"})-[:SERVES]->(japanese),(zensushi)-[:LOCATED_IN]->(jurongwest),
       (sayaka)-[:LIKES]->(zensushi),
       (emily)-[:LIKES]->(zensushi),
       (liting)-[:LIKES]->(zensushi),
       (daisy)-[:LIKES]->(zensushi),
       (malahotpot:Restaurant {name:"Mala Hot Pot"})-[:SERVES]->(chinese),(malahotpot)-[:LOCATED_IN]->(jurongnorth),
       (alice)-[:LIKES]->(malahotpot),
       (nguyenhanh)-[:LIKES]->(malahotpot),
       (liting)-[:LIKES]->(malahotpot),
       (dimsum:Restaurant {name:"Dim Sum"})-[:SERVES]->(chinese),(dimsum)-[:LOCATED_IN]->(jurongsouth),
       (alice)-[:LIKES]->(dimsum),
       (emily)-[:LIKES]->(dimsum),
       (liting)-[:LIKES]->(dimsum),
       (thaigrill:Restaurant {name:"Thai Grill"})-[:SERVES]->(thai),(thaigrill)-[:LOCATED_IN]->(jurongsouth),
       (alice)-[:LIKES]->(thaigrill),
       (judy)-[:LIKES]->(thaigrill),
       (daisy)-[:LIKES]->(thaigrill),
       (sayaka)-[:LIKES]->(thaigrill),
       (phostreet:Restaurant {name:"Pho Street"})-[:SERVES]->(vietnamese),(phostreet)-[:LOCATED_IN]->(jurongeast),
       (nguyenhanh)-[:LIKES]->(phostreet),
       (kimlee)-[:LIKES]->(phostreet),
       (emily)-[:LIKES]->(phostreet)
```

### 모든 데이터 불러오기

```cypher
MATCH (n) RETURN (n)
```

### Person에서 이름이 Alice이고 Alice가 친구인 노드의 이름 불러오기

```cypher
MATCH (alice:Person {name:"Alice"})-[:IS_FRIEND_OF]-(person)
RETURN person.name
```

### Restaurant노드와 연결된 노드 불러오기

```cypher
MATCH (location)<-[:LOCATED_IN]-(restaurant)-[:SERVES]->(cuisine)
RETURN location, restaurant, cuisine
```

### 특정 location의 restaurant노드 불러오기

```cypher
MATCH (jurongeast:Location {name:"Jurong East"})<-[:LOCATED_IN]-(restaurant)-[:SERVES]->(cuisine)
RETURN jurongeast, restaurant, cuisine
```



### Alice가 친구들과 방문할 가장 적합한 레스토랑은?

```cypher
MATCH (restaurant:Restaurant)-[:LOCATED_IN]->(location),
      (restaurant)-[:SERVES]->(cuisine),
      (person:Person)-[:LIKES]->(restaurant)
RETURN restaurant.name, collect(person.name) as likers, count(person.name) as occurence
ORDER BY occurence DESC
```

* Count() = 일치하는 레코드 수 반환



### Alice를 제외한 Alice의 친구들이 선호하는 레스토랑은?

```cypher
MATCH (alice:Person {name:"Alice"}), 
      (alice)-[:IS_FRIEND_OF]-(friend), 
      (restaurant:Restaurant)-[:LOCATED_IN]->(location),
      (restaurant)-[:SERVES]->(cuisine),
      (friend)-[:LIKES]->(restaurant)
RETURN restaurant.name, collect(friend.name) as likers, count(*) as occurence
ORDER BY occurence DESC
```



### Judy, Kim이 선호하는 레스토랑은?

```cypher
MATCH (restaurant:Restaurant)-[:LOCATED_IN]->(location),
      (restaurant)-[:SERVES]->(cuisine),
      (person:Person)-[:LIKES]->(restaurant)
WHERE person.name = "Judy" OR person.name = "Kim Lee"
RETURN restaurant.name, collect(person.name) as likers, count(*) as occurence
ORDER BY occurence DESC
```



### 약속장소에 위치한 레스토랑 중 갈만한 곳은?

```cypher
MATCH (alice:Person {name:"Alice"}),
      (alice)-[:IS_FRIEND_OF]-(friend),
      (restaurant:Restaurant)-[:LOCATED_IN]->(location:Location {name:"Jurong East"}),
      (restaurant)-[:SERVES]->(cuisine),
      (friend)-[:LIKES]->(restaurant)
RETURN restaurant.name, collect(friend.name) as likers, count(*) as occurence
ORDER BY occurence DESC
```

