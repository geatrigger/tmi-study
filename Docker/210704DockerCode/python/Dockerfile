FROM python:3
ADD test.py /usr/src
ADD wait-for-it.sh /usr/src
WORKDIR /usr/src
RUN apt-get update
RUN pip install pymysql
VOLUME ["/usr/src"]
# network는 여기서 설정 불가