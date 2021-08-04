### 1. RDBMS vs NoSQL

---

- RDBMS

  - SQL(Structured Query Language)

    데이터베이스와 상호 작용하는 데 사용하는 쿼리 언어

  - Schema

    데이터는 table에 record로 저장되며, 각 테이블에는 명확하게 정의된 구조가 있음. 구조는 field의 이름과 데이터 유형으로 정의

    RDBMS에서 스키마를 준수하지 않는 레코드는 추가 불가

    <img src="https://t1.daumcdn.net/cfile/tistory/99BF063C5C937DF324" alt="shema" style="zoom:100%;" />

  - 관계

    데이터들을 여러 테이블에 나눠서 데이터들의 중복을 피할 수 있음. 명확한 구조를 통해 현재 테이블에서는 중복없이 하나의 데이터만을 관리하기 때문에 다른 테이블에 있는 부정확한 데이터를 다룰 위험이 없음

    ![relation](https://t1.daumcdn.net/cfile/tistory/994D09355C937ECD2D)

- NoSQL

  - SQL과 반대되는 접근방식을 따르기 때문에 지어진 이름

  - 스키마, 관계 없음

    RDBMS에서의  Records  -> MongoDB에서는 Documents (다른 NoSQL에서 이름이 다른 경우 있음)

    ![NoSQL](https://t1.daumcdn.net/cfile/tistory/99FBC9415C937F2A20)

  - Collections

    RDBMS에서 여러 테이블로 나누는 것과 달리, 관련된 데이터들을 동일한 Collection에 넣음.

    아래 예시는 Orders 컬렉션에 일반적인 정보(Users, Products)를 모두 포함한 데이터를 저장한 모습

    즉, 여러 컬렉션에 join할 필요없이 이미 필요한 모든 데이터를 갖춘 상태

    NoSQL은 join개념이 존재하지 않는 대신 컬렉션을 통해 데이터를 복제하여 각 컬렉션 일부분에 속하는 데이터를 정확하게 산출하도록 함

    필요한 모든 데이터가 이미 하나의 컬렉션 안에 들어가 있기에 복잡한 조인을 사용할 필요 없음

    자주 변경되지 않는 데이터인 경우에 큰 장점 

    각 컬렉션에 중복되는 데이터가 들어가기 때문에 어디서는 수정하고 다른 컬렉션에서는 수정하지 않는 등 불안정한 측면 존재

    ![Collections](https://t1.daumcdn.net/cfile/tistory/99C57D3B5C937F5E17)

    

- 수평(horizontal) 수직(vertical)  확장(scaling)

  - 수평적 확장 : 더 많은 서버가 추가되어 데이터베이스가 전체적으로 분산됨. 하나의 데이터베이스에서 작동하지만 여러 호스트에서 작동

  - 수직적 확장 : 데이터베이스 서버의 성능을 향상

    데이터가 저장되는 방식 때문에 RDBMS는 일반적으로 수직적 확장만 지원.

    수평적 확장은 NoSQL에서만 가능

    ![scaling](https://t1.daumcdn.net/cfile/tistory/990D6E385C937F8530)

- 의사결정

  - RDBMS

    - 장점

      명확하게 정의 된 스키마, 데이터 무결성 보장

      관계는 각 데이터를 중복없이 한번만 저장

    - 단점

      상대적으로 덜 유연함. 데이터 스키마는 사전에 계획되고 알려져야 함(나중에 수정하기가 번거롭거나 불가능 할 수 있음)

      관계를 맺고 있기 때문에,  JOIN문이 많은 매우 복잡한 쿼리가 만들어 질 수 있음

      수평적 확장이 어렵고, 대체로 수직적 확장만 가능. 즉 어떤 시점에서 (처리 할 수 있는 처리량과 관련하여) 성장 한계에 직면하게 됨.

    - 언제 사용하나?

      관계를 맺고 있는 데이터가 자주 변경(수정)되는 애플리케이션일 경우 (NoSQL에서라면 여러 컬렉션을 모두 수정해야 함)

      변경될 여지가 없고, 명확한 스키마가 사용자와 데이터에게 중요한 경우

  - NoSQL

    - 장점

      스키마가 없기때문에, 훨씬 더 유연. 즉, 언제든지 저장된 데이터를 조정하고 새로운 "필드" 추가 가능

      데이터는 애플리케이션이 필요로 하는 형식으로 저장. 이렇게 하면 데이터를 읽어오는 속도가 빨라짐

      수직 및 수평 확장이 가능하므로 데이터베이스가 애플리케이션에서 발생시키는 모든 읽기 / 쓰기 요청을 처리 할 수 있음.

    - 단점

      유연성 때문에, 데이터 구조 결정을 하지 못하고 미루게 될 수 있음

      데이터 중복은 여러 컬렉션과 문서가 (SQL 세계에서 처럼 하나의 테이블에 하나의 레코드가 아니라) 여러 개의 레코드가 변경된 경우 업데이트 필요.

      데이터가 여러 컬렉션에 중복되어 있기 때문에, 수정(update)를 해야 하는 경우 모든 컬렉션에서 수행해야 함. (SQL 세계에서는 중복된 데이터가 없기 때문에 한번만 수행하면 됨.)

    - 언제 사용하나?

      정확한 데이터 구조를 알 수 없거나 변경 / 확장 될 수 있는 경우

      읽기(read)처리를 자주하지만, 데이터를 자주 변경(update)하지 않는 경우 (즉, 한번의 변경으로 수십 개의 문서를 업데이트 할 필요가 없는 경우)

      데이터베이스를 수평으로 확장해야 하는 경우 ( 즉, 막대한 양의 데이터를 다뤄야 하는 경우)

      

데이터베이스는 다른 방식으로 설계 될 수 있음. NoSQL 데이터베이스를 쓰더라도 설계적으로 언급된 단점들을 완화시킬 수 있음. (예를들면 중복된 데이터를 줄이는 방법). SQL 데이터베이스도 요구사항을 만족시키고, 복잡한 JOIN문을 만들지 않도록 설계할 수 있음.

  

### 2. MongoDB

---

1. MongoDB란?

   - NoSQL 데이터베이스
     - MongoDB, HBase 등등  NoSQL 중 가장 대표적
     
   - open source(무료이용가능)

   - Transaction(DBMS상호작용 단위)으로 ACID(안전성 우선) 대신 BASE를 선택해 가용성, 성능 우선시

     MongoDB가 전혀 ACID하지 않다는 게 아님. 버전이 업데이트 됨에 따라 트랜젝션(데이터베이스의 상태를 변화시키기 위해 수행하는 작업의 단위)을 제공하면서 ACID 충족은 물론 분산 트랜젝션도 가능해짐

     **BASE**는 ACID와 대립되는 개념으로 다음 세 가지로 이루어져있음

     - Basically Avaliable

       기본적으로 언제든지 사용할 수 있다는 의미를 가지고 있음

       즉, 가용성이 필요하다는 뜻을 가짐

     - Soft state

       외부의 개입이 없어도 정보가 변경될 수 있다는 의미를 가지고 있음

       네트워크 파티션 등 문제가 발생되어 일관성(Consistency)이 유지되지 않는 경우 일관성을 위해 데이터를 자동으로 수정함

     - Eventually consistent

       일시적으로 일관적이지 않은 상태가 되어도 일정 시간 후 일관적인 상태가 되어야한다는 의미를 가지고 있음

       장애 발생시 일관성을 유지하기 위한 이벤트를 발생시킴

     이처럼 BASE는 ACID와는 다르게 일관성을 어느정도 포기하고 가용성을 우선시함. 즉, 데이터가 조금 맞지 않더라도 일단 내려줌

     

2. MongoDB 계층구조

   ![relation](https://user-images.githubusercontent.com/37397737/70114448-d9541980-169f-11ea-808f-57daa9e6100d.png)

   - Collections

     - MongoDB Document들의 그룹
     - RDBMS의 Table과 비슷한 개념
     - 따로 스키마(schema)를 갖고 있지 않음

   - **Document**

     - Document 기반의 데이터베이스는 RDBMS와 다르게 자유롭게 데이터 구조를 잡을 수 있음

     - MongoDB는  BSON으로 데이터가 쌓여 Array 데이터나 중첩구조 데이터등을 쉽게 넣을 수 있음

     - _id 를 자동적으로 부여해 unique한 document를 가짐

       ![objectid](https://kciter.so/images/2021-02-25-about-mongodb/objectid.png)

       id : 12bytes의 hexadecimal 값, 각 document의 유일함(uniqueness)을 제공
       이 값의 첫 4bytes 는현재 timestamp, 다음 3bytes는 machine id, 다음 2bytes는 MongoDB 서버의 프로세스id, 마지막 3bytes는 순차번호.

       `ObjectId`가 충돌이 발생하려면 같은 시간, 기기에서 만들어낸 해시 값이 일치하고 우연히 같은 process id를 가지고 있으며 정말 우연히 increase된 count가 일치해야 함. 충돌날 일은 거의 없음

     - 동적 스키마를 가져 같은 Collection안의 Document들끼리 다른 데이터, 구조를 가질 수 있음

     -  key : value 쌍으로 이루어짐

   - Fields

     - RDBMS의 속성과 비슷한 개념
     - key에 해당하는 값을 말하며, 주로 조회에 사용
     
     

3. MongoDB 설치

   https://www.mongodb.com/download-center#community 

   - MongoDB
   
     Community Server 에서 설치
   
     MongoDB Compass 를 같이 설치할 수 있어서, 같이 설치되었다면 아래에 있는 Compass를 굳이 따로 설치할 필요X
   
   - MongoDB Compass
   
     ![c1](https://www.hanumoka.net/images/20181018-mongodb-install-at-windows_6.png)
   
     
   
   - MongoDB Atlas (설치참고 :  https://www.youtube.com/watch?v=C2rhqCwho)
   
     ![at1](20210721_MongoDB_basic.assets/at1.JPG)
   
     ![at2](20210721_MongoDB_basic.assets/at2.JPG)
   
     ![at3](20210721_MongoDB_basic.assets/at3.JPG)
   
     
   
      
   
     
   
   ---
   
   
   - 환경설정
   
     cmd
   
     기본 데이터베이스 디렉터리(C:\data\db)를 생성 (반드시 이렇게 생성해야 한다.)
   
     ```bash
     mkdir C:\data\db
     ```
   
     로그 파일이 저장될 디렉터리를 생성
   
     ```bash
     mkdir C:\mongodb\log
     ```
   
     mongod.cfg 환경설정 파일을 생성하여 C:\mongodb 내에 저장
   
     ```bash
     cd C:\\mongodb
     
     echo >> mongod.cfg
     ```
   
     mongod.cfg 파일을 열어서 아래와 같이 편집
   
     ```
     ##Which IP address(es) mongod should bind to.
     bind_ip = 127.0.0.1
     
     ##Which port mongod should bind to.
     port = 27017
     
     ##I set this to true, so that only critical events and errors are logged.
     quiet = true
     
     ##store data here
     dbpath=C:\data\db
     
     ##The path to the log file to which mongod should write its log messages.
     logpath=C:\mongodb\log\mongo.log
     
     ##I set this to true so that the log is not overwritten upon restart of mongod.
     logappend = true
     
     ##log read and write operations
     diaglog=3
     
     ##It ensures write durability and data consistency much as any journaling scheme would be expected to do.
     ##Only set this to false if you don't really care about your data (or more so, the loss of it).
     journal = true
     
     ##For mongodb 32 bit
     storageEngine = mmapv1
     ```
   
     MongoDB가 설치된 디렉터리로 이동한다. 설치 디렉터리를 별도 지정하지 않았다면 `C:\Program Files\MongoDB\Server\5.0\bin\`에 설치됨
   
     ```bash
     cd C:\Program Files\MongoDB\Server\5.0\bin
     ```
   
     MongoDB Server를 기동(mongod.exe)
   
     ```bash
     mongod --config c:\mongodb\mongod.cfg
     ```
   
     새로운 CMD 창에서 MongoDB Client 쉘을 실행(mongo.exe). mongod을 먼저 실행하고 실행해야 함
   
     ```bash
     cd C:\Program Files\MongoDB\Server\5.0\bin
     
     mongo
     ```
   
     
   
     **couldn't connect to server 127.0.0.1:27017, connection attempt failed** 에러 해결
   
     mongodb 서버가 실행되지 않아서 연결이 안되는 경우임
   
     ![error](https://media.vlpt.us/images/hanblueblue/post/03a61772-1e80-470c-8fa0-9ff2df9f87be/image.png)
   
     ```bash
     mongod --dbpath C:\data\db
     ```
   
     ![fix](https://media.vlpt.us/images/hanblueblue/post/ed04af8c-6ba8-4eaa-8d6b-5f290ccd5dc2/image.png)
   
     ~$로 나오지 않으면 성공이다.
   
     다시 새 cmd창에서 mongo명령어로 클라이언트 실행 후, 어떤 데이터베이스도 생성되지 않는 상태에서 db명령어를 입력했을 때 test 결과가 출력되면 연결에 성공한 것임
   
     - 관리자 권한이 있는 계정 생성
   
       ```bash
       use admin
       
       db.createUser({user:'statice', pwd:'1008', roles:['root']})
       ```
       
       
     
     - DB 중지하는법
     
         MongoDB 클라이언트를 기동시킨 CMD창에서 admin 데이터베이스로 변경한 후 DB를 중지시킴. 이때 MongoDB 서버 또한 중지됨
     
         ```bash
         show dbs
         
         use admin
         
         db.shutdownServer()
         
         quit()
         ```
     
     
     
     ---
     
   - MongoDB Compass로 서버 접속
   
     위에서 서버가 실행되고 있는 cmd창 등에서도 코딩이 가능하지만, 조작하는데 환경이 불편함
     
     설치한 MongoDB compass를 이용해 관리하는게 편함.
     
     
     
     Connect옵션 중 **Fill in connection fields individually** 를 클릭해 위에서 생성한 계정을 입력해 접속할 수 있다.
     
     ![compass](https://www.hanumoka.net/images/20181018-mongodb-install-at-windows_12.png)
   
   
   
   
   
   
   - MongoDB Atlas와 Compass연결
   
     connect your application 클릭해 connection string 생성 및 복사
     
     ![at4](20210721_MongoDB_basic.assets/at4.JPG)
     
     <password> 부분을 실제 패스워드로 바꾼 후 입력한다음 Connect를 누르면 Atlas에서 생성된 sample db가 MongoDB Compass에 연결됨
     
     ![connection](20210721_MongoDB_basic.assets/connection.JPG)





2. 데이터 조작(CRUD 기본)

   | RDB(MySQL)                                                | MongoDB                                                      |
   | --------------------------------------------------------- | ------------------------------------------------------------ |
   | Insert                                                    |                                                              |
   | insert into users ("name", "city") values("lee", "seoul") | db.users.insert({ name: "lee", city: "seoul" })              |
   | Select                                                    |                                                              |
   | select * from users where name="lee"                      | db.users.find({ name: "lee" })                               |
   | Update                                                    |                                                              |
   | update users set city="busan" where name="lee"            | db.users.update({ name: "lee" }, { $set: { city: "busan" }}) |
   | Delete                                                    |                                                              |
   | delete from users where name="lee"                        | db.users.remove({ name: "lee" })                             |

   

  - Nosql이므로 sql을 사용하지 않고 별도로 제공하는 API를 통해 데이터를 건들 수 있음

  - 기본적으로 자바스크립트 엔진 SpiderMonkey를 사용하여 API제공함

  - MongoDB 내에 있는 MongoDB Shell을 이용하여 JavaScript 실행이 가능함.

    

    1. Create

       현재 사용중인 database 확인

       ```bash
       db
       ```

       database 리스트 확인

       ```bash
       show dbs
       ```

       db의 collection에 document 를 삽입하는법

       ```bash
       db.books.insert({ title: "Example1", author: "Lee", price: 100 })
       ```

       한번에 여러 개의 document를 insert가능

       ```bash
        db.books.insert([
         { title: "E1", author: "L1", price: 200 },
         { title: "E2", author: "L2", price: 300 },
         { title: "E3", author: "L3", price: 400 }
         ])
       ```

    2. Read

       현재 사용중인 db 변경

       ```bash
       use sample_mflix
       ```

       collection list 확인

       ```bash
       show collections
       ```

       collection 내의 모든 document를 select

         projection 생략 시  모든 field가 선택됨

       ```bash
       db.movies.find()
       ```

       

       collection 내의 특정 document를 select

       ​     **db.collection.find(query, projection)**

       ​         query : sql의 where절과 유사.

       ​          projection : document select 결과에 포함될 field

       _id는 지정하지 않아도 출력에 포함되므로 select할 field에 포함시키지 않을 경우에는 projection의 해당 field의 value에 0을 지정하여 명시적으로 배제

       ```bash
       db.movies.find({countries:'USA'},{_id:0,countries:1,directors:1})
       ```

       

       비교 연산자를 사용해 조건에 맞는 document를 select

       ```bash
       db.theaters.find({theaterId:{$gt:1000, $lte: 1005}})
       ```

       **비교 연산자**

       | Operator | Meaning                | Description                   |
       | :------- | :--------------------- | :---------------------------- |
       | $eq      | equals                 | 지정 값과 일치하는 값         |
       | $gt      | greater than           | 지정 값보다 큰 값             |
       | $gte     | greater than or equals | 지정 값보다 크거나 같은 값    |
       | $lt      | less than              | 지정 값보다 작은 값           |
       | $lte     | less than or equals    | 지정 값보다 작거나 같은 값    |
       | $ne      | not equal              | 지정 값과 일치하지 않는 값    |
       | $in      | in an array            | 지정 배열 안에 속하는 값      |
       | $nin     | none in an array       | 지정 배열 안에 속하지 않는 값 |

       

       논리 연산자를 사용해 조건에 맞는 document를 select

       ```bash
       db.theaters.find({$and:[{theaterId:{$gt:1000, $lte: 1005}},{"location.address.city":"California"}]})
       ```

       **논리 연산자**

       | Operator | Description                                |
       | -------- | ------------------------------------------ |
       | $or      | 지정 조건중 하나라도 true이면 true         |
       | $and     | 모든 지정 조건이 true이면 true             |
       | $not     | 지정 조건이 false이면 true, true이면 false |
       | $nor     | 모든 지정 조건이 false이면 true            |

       

       이렇게 조건으로 뽑아낸 documents들을 객체에 지정할 수도 있음

       ```bash
       a = db.theaters.find({theaterId:{$gt:1000, $lte: 1005}})
       
       a
       ```

       

    3. Update

       직접 해당 경로로 들어가서 [Edit Document]를 클릭해 Update할 수 있음

       or

       ```bash
       db.<collection_name>.update(
         <query>,
         <update>,
         {
           upsert: <boolean>,
           multi: <boolean>,
           writeConcern: <document>
         }
       )
       ```

       | Parameter    | Type     | Description                                                  |
       | ------------ | -------- | ------------------------------------------------------------ |
       | query        | document | update를 위한 selection criteria(기준)이다. find()의 query와 같다. SQL의 WHERE절과 유사하다. |
       | update       | document | document에 update할 수정 사항이다.                           |
       | upsert       | boolean  | Option(Default: false) true로 설정하면 query criteria에 매칭하는 document가 없을 경우 새로운 document를 insert한다. false로 설정하면 insert하지 않는다. |
       | multi        | boolean  | Option(Default: false) true로 설정하면 query criteria에 매칭하는 document 모두를 update한다. false로 설정하면 하나의 document만 update한다. |
       | writeConcern | document | Option. database에 write(insert, update, remove) 처리를 영속화시키기 위한 설정이다. 기본 설정을 사용하려면 이 설정을 생략한다. |

       update 부분에 들어가는 내용

       | Operator     | Description                                                  |
       | ------------ | ------------------------------------------------------------ |
       | $inc         | field의 value를 지정한 수만큼 증가시킨다.                    |
       | $rename      | field 이름을 rename한다.                                     |
       | $setOnInsert | update()의 upsert가 true로 설정되었을 경우, document가 insert될 때의 field value를 설정한다. |
       | $set         | update할 field의 value를 설정한다.                           |
       | $unset       | document에서 설정된 field를 삭제한다                         |
       | $min         | 설정값이 field value보다 작은 경우만 update한다.             |
       | $max         | 설정값이 field value보다 큰 경우만 update한다.               |
       | $currentDate | 현재 시간을 설정한다                                         |

       

       모든 document의 field name을 “ttle”에서 “title”로 rename

       ```bash
       db.test.insert([
         { ttle: "Example1", author: "Lee", price: 200 },
         { ttle: "Example2", author: "Lee", price: 300 },
         { ttle: "Example3", author: "Lee", price: 400 }
       ])
       
       
       db.test.update(
         {},
         { $rename: { "ttle": "title" } },
         { multi: true }
       )
       ```

       

       

    4. Delete

       직접 해당 경로로 들어가서 [Delete Document]를 클릭해 Delete할 수 있음

       or

       ```bash
       db.collection.remove(
         <query>,
         {
           justOne: <boolean>,
           writeConcern: <document>
         }
       )
       ```

       | Parameter    | Type     | Description                                                  |
       | ------------ | -------- | ------------------------------------------------------------ |
       | query        | document | deletion criteria(기준)이다. collection 내의 모든 document를 삭제할 경우, {}를 전달한다. |
       | justOne      | boolean  | Option(Default: false) true로 설정하면 하나의 document만 삭제한다. 생략하면 deletion criteria에 매칭하는 document 모두를 삭제한다. |
       | writeConcern | document | Option. database에 write(insert, update, remove) 처리를 영속화시키기 위한 설정이다. 기본 설정을 사용하려면 이 설정을 생략한다. |

       price가 300보다 큰 모든 document를 삭제

       ```bash
       db.test.remove({price:{$gt:300}})
       ```

       

       collection의 모든 document 삭제

       ```bash
       db.collection.remove({})
       ```

       collection 삭제

       ```bash
       db.collection.drop()
       ```

       database 삭제

       ```bash
       db.dropDatabase();
       ```

  













