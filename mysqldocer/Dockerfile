FROM mysql

ENV MYSQL_ROOT_PASSWORD=sahil

RUN mkdir /data

EXPOSE 3306

#docker buildx build --tag mysql:latest .
# above command to build the image
#use below command to run the container .
#d

#docker run --name mysql_retail -e MYSQL_ROOT_PASSWORD=sahil -d -v /Users/sahiltayde/appdata/mywork/itversity/mysql_retail_db/retail_mysql_db:/retail_db -p 3306:3306 mysql:latest 
#stop the docker
#docker exex -t (contailer_name) /bin/bash
#-->inside docker run { mysql -u root -p }
#docker stop mysql_retail

#mysql> CREATE DATABASE retail;
#Query OK, 1 row affected (0.13 sec) mysql> CREATE USER retail_user IDENTIFIED BY 'sahil';
#Query OK, 0 rows affected (0.08 sec) mysql> GRANT ALL ON retail.* TO retail_user;
#Query OK, e rows affected (0.08 sec) mysql> FLUSH PRIVILEGES;
#Query oK, e rows affected (0.06 sec)
#use retail ;
#show databases;
#show tables;
#SOURCE /retail_db/create_db.sql
#ocker exec -it mysql_retail mysql -u retail_user -p -D retail