<< Docker 실습 >>
 


▲ docker 설치

ㅇ 패키지 인덱스 정보 업데이트
$ sudo apt-get update

ㅇ debian 계열에서 설치 및 삭제
$ sudo apt-get install docker.io
$ sudo apt remove --purge docker docker-engine docker.io

ㅇ 자동스크립트를 이용하는 방법    -  가장 쉽다.
$ curl -fsSL https://get.docker.com/ | sudo sh

ㅇ docker 를 sudo 없이 사용가능하게 하려면
$ sudo usermod -aG docker ${USER}
$ sudo service docker restart



▲ Mac, Windows 에 Docker 설치하기
Docker For Mac, Docker For Windows 를 설치하면 된다.
하지만 docker 는 리눅스 컨테이너이므로 windows > 가상머신 > 리눅스커널 > 도커 순서로 설치가 된다. 포트를 연결하기 위해서는 도커 컨테이너의 특정포트를 가상머신에 연결하고 다시 mac이나 windows 에 포트에 연결되는 구조이다. 
개념을 이해하기 위해서라면 리눅스에 설치하는 것이 좋을 듯 하다.


▲  docker  version 
ㅇ Docker version 확인
$ docker version
$ docker info



▲  Docker  첫 실행
ㅇ Docker version 확인
$ docker version

ㅇ hello-world 실행
$ docker run hello-world
local에 존재하는 image를 실행한다.
만약, 존재하지 않으면 docker hub에서 찾아서 존재하는 경우 pull, run 되는 구조임

$ docker images 로 확인

ㅇ ubuntu 실행
$ docker run ubuntu:16.04
image 를 받은 적이 없기때문에 받아서(pull) 컨테이너를 생성(create), 시작(start)한다.
컨테이너는 프로세스이기 때문에 실행중인 프로세스가 없으면 컨테이너는 종료된다.

/bin/bash 명령어를 입력하여 컨테이너 실행
$ docker run --rm -it ubuntu:16.04 /bin/bash

ㅇ 컨테이너 프로세스 확인(2번 터미널을 하나 더 실행하여)
$ docker ps -a
$ docker images

ㅇ 컨테이너 종료후 이미지 삭제 
docker rm [ubuntu_ct_id]   -- 컨테이너 삭제
docker rmi ubuntu:16.04   -- 이미지 삭제

▲  mysql 실행
ㅇ 실행
$ docker run -d -p 3306:3306 \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=true \
  --name mysql \
  mysql:5.7

데몬(-d) 으로 실행됨

$ docker exec -it mysql /bin/bash   ← exec 는 실행중인 mysql 컨테이너에 명령 수행
$ mysql -uroot
$ show databases

$ docker exec -it mysql bash
$ docker exec -it mysql mysql -uroot   ← 쉘 권한을 얻는 방법말고 바로 mysql 수행
$ show databases

ㅇ 포트확인
$ netstat -nplt

ㅇ 컨테이너 종료(stop), 삭제(rm), 이미지삭제(rmi)
$ docker stop [컨테이너ID]
$ docker rm [컨테이너ID]
$ docker rmi mysql:5.7


 

▲ nginx
ㅇ 실행
$ docker run --name nginx -d -p 80:80 nginx

ㅇ 확인
http://18.136.103.92
 

ㅇ 내부작업
$ docker exec –it nginx /bin/bash
$ cd /etc/nginx
$ apt-get update
$ apt-get install vim
$ vi nginx.conf


ㅇ 컨테이너 종료(stop), 삭제(rm), 이미지삭제(rmi)
$ docker stop [컨테이너ID]
$ docker rm [컨테이너ID]
$ docker rmi nginx








▲  docker 명령들 : search, images, pull, run ps, rm, rmi

ㅇ docker store 에서 검색
$ sudo docker search mysql
$ sudo docker search ubuntu
pi@raspberrypi:~ $ sudo docker search ubuntu
NAME                                                      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                                                    Ubuntu is a Debian-based Linux operating s...   8141      [OK]
dorowu/ubuntu-desktop-lxde-vnc                            Ubuntu with openssh-server and NoVNC            205                  [OK]
rastasheep/ubuntu-sshd  

ㅇ image 목록
$ sudo docker images
pi@raspberrypi:~ $ sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
ubuntu              16.04               2322c4e864c9        2 weeks ago         114.8 MB
ubuntu              latest              b03924df2b7e        2 weeks ago         83.48 MB

ㅇ image 삭제
$ sudo docker rmi b03924df2b7e 

ㅇ pull : docker hub(public or private) 에서 image 가져오기
$ sudo docker pull ubuntu
pi@raspberrypi:~ $ sudo docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
9089496db59f: Pulling fs layer
628d96b94ccc: Pulling fs layer
1246ca2bbfe7: Pulling fs layer
cf6569441466: Pulling fs layer
fd116dfc2baa: Pulling fs layer
b03924df2b7e: Pulling fs layer
$ sudo docker pull ubuntu:16.04

※ 아래는 실패 사례 - 라즈베리파이에서 ARM 호환이 맞지 않아 발생한것으로 추정
$ sudo docker pull hypriot/rpi-mysql 
$ sudo docker pull hypriot/rpi-mysql:5.5
$ sudo docker pull hypriot/rpi-mysql:latest
pi@raspberrypi:~ $ sudo docker pull hypriot/rpi-mysql
Using default tag: latest
Pulling repository docker.io/hypriot/rpi-mysql
Tag latest not found in repository docker.io/hypriot/rpi-mysql
왜 에러가 날까??

$ sudo docker pull tobi312/rpi-nginx  ← 실패
$ sudo docker pull tobi312/rpi-nginx:1.10  ← 실패
$ sudo docker pull hypriot/rpi-python  ← 성공


ㅇ  run 

docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]

ㅇ 자주 사용하는 옵션들
옵션	설명
-d	detached mode 흔히 말하는 백그라운드 모드
-p	호스트와 컨테이너의 포트를 연결 (포워딩)
-v	호스트와 컨테이너의 디렉토리를 연결 (마운트)
-e	컨테이너 내에서 사용할 환경변수 설정
--name	컨테이너 이름 설정
--rm	프로세스 종료시 컨테이너 자동 제거
-it	-i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션
--link	컨테이너 연결 [컨테이너명:별칭]



$ docker run hello-world
$ docker run --rm -it ubuntu:16.04 /bin/bash

※  라즈베리에서 run 실패사례
$ sudo docker run  ubuntu:16.04  ← 실패 : exec format error
$ sudo docker run  ubuntu  ← 실패 : exec format error

pi@raspberrypi:~ $ sudo docker run  ubuntu
WARNING: Your kernel does not support memory swappiness capabilities, memory swappiness discarded.
exec format error
Error response from daemon: Cannot start container 83ce36ca2e275a991340cc51531249920d9989dff49169492ce60e153cb8cb82: [8] System error: exec format error

$ docker run --name python -d  hypriot/rpi-python

ㅇ exec   : 실행 중인 도커 컨테이너 내부에 접속
docker exec -i -t <CONTAINER ID> /bin/bash
$ docker exec -it mysql bash
$ docker exec -it hypriot/rpi-python bash




ㅇ stop : 도커 컨테이너 
$ docker stop -f ba619b0c2a1e
ba619b0c2a1e는 docker ps를 통해 얻어진 container id 값이다.


ㅇ 도커 호스트의 모든 컨테이너 삭제
docker rm $(docker ps -a -q)


ㅇ 도커 로그
docker logs <CONTAINER ID>    ← 모든 로그를 다 보여준다.
docker logs -f <CONTAINER ID>   ← 마지막 로그보여주고 대기
docker logs --tail=3  <CONTAINER ID>    ← 마지막 3줄만 보여주기

ㅇ 기타
docker version
docker info
docker inspect 컨테이너ID
docker stats 컨테이너ID
docker events
docker top 컨테이너ID
docker history 이미지ID



▲ container 목록, 삭제
ㅇ container 목록
 $ sudo docker ps
 $ sudo docker ps -a
pi@raspberrypi:~ $ sudo docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
cae4ff4482bb        ubuntu:16.04        "/bin/bash"         11 minutes ago      Created                                 grave_thompson
83ce36ca2e27        ubuntu              "/bin/bash"         4 hours ago         Created                                 boring_brown
c4116bcbfaa8        ubuntu:16.04        "/bin/bash"         4 hours ago         Created                                 insane_yalow

ㅇ container 삭제 
sudo docker rm [OPTIONS] CONTAINER [CONTAINER...]container rm 
$ sudo docker rm 83ce36ca2e27 
pi@raspberrypi:~ $ sudo docker rm 83ce36ca2e27
83ce36ca2e27

ㅇ 종료된 컨테이너 일괄삭제
docker rm -v $(docker ps -a -q -f status=exited)


< Docker 사례 >
▲ tensorflow 예제
$ docker run -d -p 8888:8888 -p 6006:6006 teamlab/pydata-tensorflow:0.1
$ docker run -it -p 8888:8888 -p 6006:6006 teamlab/pydata-tensorflow:0.1


< Docker-compose 로 실행 >
▲ 컨테이너를 실행할때 docker compose를 이용하면 힘들게 명령어를 기이일게 입력하지 않아도 되고 컨테이너간 의존성도 알아서 체크하여 순서대로 실행해줍니다.

▲ docker-compose

ㅇ docker-compose 설치
sudo apt install docker-compse        or
curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
# test
docker-compose version



ㅇ wordpress 를 compose를 이용해 만들기
-	DB 준비
# mysql 실행
docker run -d -p 3306:3306 \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=true \
  --name mysql \
  mysql:5.7

# create mysql database
$ mysql -h127.0.0.1 -uroot
create database wp CHARACTER SET utf8;
grant all privileges on wordpress.* to wordpress@'%' identified by 'wordpress';
flush privileges;
quit


# mysq 실행
docker run -d -p 3306:3306 \
  -e MYSQL_ALLOW_EMPTY_PASSWORD=true \
  --name mysql \
  mysql:5.7


# 환경변수 참고
  -e MYSQL_ROOT_PASSWORD=wordpress \
  -e MYSQL_DATABASE-e wordpress \
  -e MYSQL_USER-e wordpress \
  -e MYSQL_PASSWORD-e wordpress \




-	docker-compose.yml 파일 만들기
version: '2'

services:
   db:
     image: mysql:5.7
     volumes:
       - db_data:/var/lib/mysql
     restart: always
     environment:
       MYSQL_ROOT_PASSWORD: wordpress
       MYSQL_DATABASE: wordpress
       MYSQL_USER: wordpress
       MYSQL_PASSWORD: wordpress

   wordpress:
     depends_on:
       - db
     image: wordpress:latest
     volumes:
       - wp_data:/var/www/html
     ports:
       - "8000:80"
     restart: always
     environment:
       WORDPRESS_DB_HOST: db:3306
       WORDPRESS_DB_PASSWORD: wordpress
volumes:
    db_data:
    wp_data:



-	실행 : docker-compose up

▲ Docker  image 만들기

ㅇ Dockerfile 생성
$ cat Dockerfile
# 1. java 설치 (패키지 업데이트 + 만든사람 표시)
FROM       java
MAINTAINER ssongmantop@gmail.com
RUN        apt-get -y update

# 2. 소스 복사
COPY . /usr/src/app

# 3. 실행 디렉토리 설정
WORKDIR /usr/src/app

# 4. App 서버 실행 (Listen 포트 정의)
EXPOSE 8080
CMD    java -jar ReadingList-0.0.1-SNAPSHOT.jar


ㅇ Docker build   --  image 만들기

[docker file 이 있는 곳에서]
docker build [OPTIONS] PATH | URL | -

$ docker build -t app  .                            ← okay 잘됨
$ docker build -f Dockerfile -t app . 
$ docker build -f Dockerfile -t ssongman/app . 



▲ image 를 이동할때
$ docker export
$ docker save



< Docker 기타 명령어 >

▲docker cp  : 호스트의 파일을 컨테이너로, 혹은 그 반대로 copy  할 수 있다.
$ docker cp ./nginx2.conf  940a4a5eca2d:/etc/nginx

▲docker pause : 컨테이너의 실행을 일시 정지. 
nginx 의 경우 서버시가 중지되며 client 에서는 무한 대기함
docker unpause 로 해지 가능




< blue-green 무중단 배포 >
▲ 두개의 실행파일 만들기
docker-compose-blue.yml
docker-compose-green.yml

ㅇ CD 를 위한 배포 쉘
 
https://www.youtube.com/watch?v=ZM9sU3nqCMM&t=415s



#!/bin/sh

TARGET_DEPLOY_TCP=tcp://192.168.0.100:2375
DOCKER_APP_NAME=likehs

EXIST_BLUE=$(DOCKER_HOST=${TARGET_DEPLOY_TCP} docker-compose -p ${DOCKER_APP_NAME}-blue -f docker-compose.blue.yml ps | grep Up)

if [ -z "$EXIST_BLUE" ]; then
    DOCKER_HOST=${TARGET_DEPLOY_TCP} docker-compose -p ${DOCKER_APP_NAME}-blue -f docker-compose.blue.yml pull
    DOCKER_HOST=${TARGET_DEPLOY_TCP} docker-compose -p ${DOCKER_APP_NAME}-blue -f docker-compose.blue.yml up -d

    sleep 10

    DOCKER_HOST=${TARGET_DEPLOY_TCP} docker-compose -p ${DOCKER_APP_NAME}-green -f docker-compose.green.yml down
else
    DOCKER_HOST=${TARGET_DEPLOY_TCP} docker-compose -p ${DOCKER_APP_NAME}-green -f docker-compose.green.yml pull
    DOCKER_HOST=${TARGET_DEPLOY_TCP} docker-compose -p ${DOCKER_APP_NAME}-green -f docker-compose.green.yml up -d

    sleep 10

    DOCKER_HOST=${TARGET_DEPLOY_TCP} docker-compose -p ${DOCKER_APP_NAME}-blue -f docker-compose.blue.yml down
fi

https://subicura.com/2016/06/07/zero-downtime-docker-deployment.html






< Docker network >

▲ 네트워크 구성
ㅇ 명령어들
docker network create airhacks
docker network remove airhacks
docker network inspect airhacks - 어떤 컨테이너가 속해 있는지 볼수 있음
docker run -d --net airhacks --name ping1 airhacks/tomme-ping



▲ 샘플
$ docker network create -d bridge --subnet 192.168.0.0 --gateway 192.168.0.1 my_network

▲ 


< Docker cheat >


▲ docker cheat 

docker build -t friendlyhello .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello  # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
docker container ls                                # List all running containers
docker container ls -a             # List all containers, even those not running
docker container stop <hash>           # Gracefully stop the specified container
docker container kill <hash>         # Force shutdown of the specified container
docker container rm <hash>        # Remove specified container from this machine
docker container rm $(docker container ls -a -q)         # Remove all containers
docker image ls -a                             # List all images on this machine
docker image rm <image id>            # Remove specified image from this machine
docker image rm $(docker image ls -a -q)   # Remove all images from this machine
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry



▲ 


▲ 


 
