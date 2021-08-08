#### ip주소, port 번호



- IP 주소                 

  내 IP주소 확인법

  cmd창에 **ipconfig** 입력 - IPv4 주소가 내 IP주소 (ex) 무선LAN : 192.168.3.3, 이더넷 WSL : 172.18.112.1)

  1. IPv4                                        

     현재 IP 주소 버전. 마침표로 구분된 네 개의 숫자로 작성되며 8비트씩 총 32비트로 구성된다. 

  2. IPV6

     현재 사용하고 있는 IP 주소 체계인 IPv6의 주소 부족 문제를 해결하기 위해 개발

     128비트의 긴 주소를 사용하여 주소 부족 문제 해결, IPv4에 비해 자료 전송 속도도 빠름

     

- port 번호

  웹브라우저를 이용하여 인터넷상에 있는 서버에 접속할 때 컴퓨터에 있는 웹브라우저 프로그램과 서버에 있는 웹서버 프로그램간을 연결해주는 플러그와 같은 역할

  <img src="https://t1.daumcdn.net/cfile/tistory/991FF14A5B25CC1C1C" alt="port" style="zoom:200%;" />

   위 그림에서는 웹 브라우저로 서버에 접속을 하면 서버의 **80** 번 포트를 가진 프로그램에 접속

  메일을 확인하기 위해 메일 서버에 접속하기 위해서 **110** 번 포트 사용

  특정 프로그램에 SSH 접속을 할 경우 **22** 번 포트 사용(SSH : 원격지 호스트 컴퓨터에 접속하기 위해 사용되는 인터넷 프로토콜)

  (수업에서는 SSH 접속프로그램으로 PUTTY 사용, 그림에서도 PUTTY를 사용하는 모습)

  

  즉, IP 주소는 컴퓨터를 찾을 때 필요한 주소, port번호는 컴퓨터 안에서 프로그램을 찾을 때 필요한 번호

  

  - 주요 Port 번호

    TCP, UDP 구분 정리까지는 안함. (참고 : https://hakjjin.tistory.com/590)
    
    | port 번호 |   protocol   |                             용도                             |
    | :-------: | :----------: | :----------------------------------------------------------: |
    |    20     |     FTP      |                    FTP - 데이터 전송 포트                    |
    |    21     |     FTP      |                        FTP - 제어포트                        |
    |    22     |     SSH      |    Secure Shell - ssh, sftp 같은 프로토콜 및 포트 포워딩     |
    |    23     |    Telnet    |         텔넷 프로토콜 - 암호화 되지 않은 텍스트 통신         |
    |    25     |     SMTP     |    Simple Mail Transfer Protocol - 이메일  전송 프로토콜     |
    |    53     |     DNS      | Domain Name System - 호스트의 도메인 이름을 네트워크 주소로 변환, 반대도 수행 |
    |    80     |     HTTP     |    HyperText Transfer Protocol - 웹 페이지 전송 프로토콜     |
    |    123    |     NTP      |         Network Time Protocol - 시간동기화 프로토콜          |
    |    443    |    HTTPS     |        HyperText Transfer Potocol over Secure Sockets        |
    |    514    |    Syslog    |                  시스템 로그 전송 프로토콜                   |
    | 1433,1434 |    MS-SQL    | JDBC 연결 문법 : jdbc:sqlserver://172.10.0.10:1433;database=[database name]; |
    | 1521,1522 |    Oracle    | JDBC 연결 문법 : jdbc:oracle:thin:@172.10.0.10:1521:[database name] |
    |   3306    |    MySQL     | JDBC 연결 문법 : jdbc:mysql://172.10.0.10:3306/[database name] |
    |   27017   |   MongoDB    |                          기본 포트                           |
    |   27018   |   MongoDB    |                           shardsvr                           |
    |   27019   |   MongoDB    |                          configsvr                           |
    |   2181    | Hadoop/Hbase |        ZooKeeper(hbase.zookeeper.property.clientPort)        |
    |   60000   | Hadoop/Hbase |                  Master(hbase.master.port)                   |
    |   60010   | Hadoop/Hbase |                Master(hbase.master.info.port)                |
    |   60020   | Hadoop/Hbase |         Region server(hbase.regionserver.info.port)          |
    |   60030   | Hadoop/Hbase |         Region server(hbase.regionserver.info.port)          |
    |   8080    | Hadoop/Hbase |                REST server(hbase.rest.port**)                |
    |   8085    | Hadoop/Hbase |              REST server(hbase.rest.info.port*)              |
    |   9090    | Hadoop/Hbase |       Thrift server(hbase.regionserver.thrift.port**)        |
    |   9095    | Hadoop/Hbase |            Thrift server(hbase.thrift.info.port*)            |

    - JDBC(Java Database Connectivity) 연결 문법 

      로컬에서 연결 시 : localhost or 127.0.0.1 

      외부 연결 시 : 해당 외부 아이피

      172.10.0.10 아이피로 예를 들어 작성 (ip주소:포트번호)

    

- Protocol

  서로 다른 기기들 간의 데이터 교환을 원활하게 수행할 수 있도록 표준화 시켜 놓은 통신 규약

  

- TCP/IP

    인터넷에 연결된 서로 다른 기종의 컴퓨터들이 데이터를 주고받을 수 있도록 하는 표준 프로토콜

    - TCP/IP의 각 계층 별 주요 프로토콜

      응용 계층 : FTP, SMTP, **TELNET**, SNMP, DNS, HTTP

      전송 계층 :  **TCP**, **UDP**, RTCP

      인터넷 계층 : **IP**, ICMP, IGMP, ARP, RARP

    

    주로 포트를 사용하는 프로토콜은 전송 계층 프로토콜. 즉, 포트 또한 전송 제어 프로토콜(TCP)와 사용자 데이터그램 프로토콜(UDP)가 관리한다.

    TCP : 양방향 통신, 중간에 데이터 유실이나 흐름 장애시 재전송을 통한 패킷 순서를 확인하고 재조립하여 사용자에게 보여주는 역할

    UDP : 단방향 통신. 상대방의 응답을 확인하지 않고 무조건 보내거나 무조건 받는 통신을 하기 때문에 데이터의 유실이 생길 수 있어 신뢰성을 보장하지 않음. 그만큼 TCP보다 속도는 빠름

    

    TCP/IP 인터넷 계층 IP -> 전송 계층 TCP, UDP -> 응용 계층 FTP, DNS, HTTP 등

    

    

    - 노출된 데이터베이스, 포트 이슈

      https://m.boannews.com/html/detail.html?idx=50868

      16년 기준 인터넷에 연결된 천만 개 이상의 시스템과 포트가 사실상 활짝 열려 있는 것으로 프로젝트 소나라는 대단위 스캐닝 프로젝트를 통해 밝혀냄

      전 세계적으로 1천 1백 2십만 개의 포트가 열려있어 공격자들이 마음만 먹으면 관계형 데이터베이스에 얼마든지 접근 가능, 1천 5백만개의 텔넷 서비스 역시 활짝 열려 있음

      스캐닝 작업은 3306 포트의 MySQL과 1433 포트의 SQL 서버만을 대상으로 했다. “MySQL의 경우 7백 8십만 개, SQL 서버의 경우 3백 4십만 개의 노출된 데이터베이스 서비스를 발견할 수 있었다. 단 두 가지 유형에서 이렇게나 많은 수의 시스템에 접근할 수 있었다면, 실제로는 엄청난 시스템 및 데이터베이스가 인터넷을 통해 접근이 가능하다는 것

      데이터가 이렇게 인터넷에 열려 있으면 공개되면 안되는 민감한 정보가 노출, 서버로의 DoS공격 역시 가능해짐. 데이터 자체에 암호화를 거는 기술은 악성 공격 및 사고로 잠깐 데이터가 노출되는 것에 대한 방어기제이지 인터넷에 꾸준히 노출되어 있는 상황에서의 보호장치는 아님

      이번 프로젝트를 통해 드러난 좋은 소식도 있다. **“SSH 사용률이 꾸준히 증가하고 있는 추세입니다. 텔넷보다 안전한 SSH 서버를 더 많이 운영하고 있는 지역이 50%를 넘어섰습니다. 텔넷은 내려가고 있고 SSH가 떠오르고 있다는 게 확연히 눈에 띈 것이죠** 물론 아직 텔넷 서버가 세상에 수천만 개 이상 존재하고 있기는 하지만요.” 또한 HTTPS 포트가 어느 덧 2위 포트로 올라서기도 했다.

      

    - 왜 SSH를 사용하나?
      - TELNET과 SSH의 공통점 : 원격지 PC를 엑세스하기 위한 용도로 사용

      - TELNET과 SSH의 차이점 : 서버와 클라이언트 간에 데이터를 주고 받는 방법이 다름

        telnet은 byte스트림 형식으로 주고 받지만 ssh의 경우에는 암호화 하여 처리한다

        중간에 누가 데이터를 채간다 하더라도 telnet과는 달리 ssh는 데이터의 안정성을 확보할수 있다.

        때문에 정보가 노출될 수 있는 telnet보다는 정보의 안정성을 어느정도 책임질수 있는 (게다가 속도차이도 나지 않기 때문에) ssh을 많이 사용한다.

      

















