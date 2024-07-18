
show databases;

create database Pet_Care;
use Pet_Care;
create table Dog( Dog_Name varchar(30) primary key, Dog_color varchar(30) not null, Dog_Age int not null, Dog_Description varchar(30) not null);
desc Dog;
create table Cat( Cat_Name varchar(30) primary key, Cat_color varchar(30) not null, Cat_Age int not null, Dog_Description varchar(30) not null);
desc Cat;
create table Pet_Guardians(user_name varchar(30) primary key, Adopted_Dog varchar(20)  references Dog(Dog_Name), Adopted_Cat varchar(20)  references Cat(Cat_Name),
							User_Address varchar(30) not null, Contact_Number bigint, Email_ID varchar(30), Confirmation enum('yes', 'no') not null);
desc Pet_Guardians;
drop table contact_us;
create table contact_us (ID int primary key auto_increment, name varchar(30) not null,email varchar(30) unique, message  varchar(50));
desc Pet_Guardians;


select * from contact_us;
delete from contact_us where id=1;


create table User(user_id varchar(30) primary key, name varchar(100) NOT NULL, email varchar(100) NOT NULL, password varchar(255) not null);
select * from contact_us;

create table resister(user_id int auto_increment primary key, username varchar(255) not null, email varchar(255) not null, password varchar(255) not null);

CREATE USER 'Pet_Care '@'localhost' IDENTIFIED BY '1234567';

SELECT user, host FROM mysql.user WHERE user = 'Pet_Care ';#This will show you the host(s) associated with the 'Pet_Care ' user.

#Syntax: SELECT user, host FROM mysql.user;
#Remember to run these queries with a user account that has the necessary privileges to access the mysql database and user table, such as the MySQL root user.

GRANT ALL PRIVILEGES ON *.* TO 'Pet_Care '@'localhost';
commit;
use Pet_Care;
