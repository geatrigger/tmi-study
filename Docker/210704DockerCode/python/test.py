import pymysql
import sys

with open('./version.txt', 'w', encoding='utf-8') as f:
  f.write(sys.version + '\n')

conn = pymysql.connect(
  host='mysql', 
  port=3306, 
  user='root', 
  password='root',
  db='testdb'
)
cur = conn.cursor()

sql = '''drop table if exists test;'''
cur.execute(sql)
sql = '''
create table test(
  name varchar(20) primary key,
  num int not null
);'''
cur.execute(sql)
sql = '''
insert into test(name, num) values("Kim", 10);
'''
cur.execute(sql)
conn.commit()
conn.close()
