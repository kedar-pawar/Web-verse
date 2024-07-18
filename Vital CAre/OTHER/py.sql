create database School;
show databases;
drop database School; 
use School;
SHOW TABLES;
create table Course(cno int primary key, cname varchar(25) not null, duration int not null, fees int default"60000");
truncate student;
insert into course value (1,"Btech Computer Science", 4, default),(2,"BCA",3,33000),(3,"Btech food technology",2,66000),(4,"Btech Agriculture",4,70000);
select * from course;
drop table Student_fees;
create table Student( Rno BIGINT primary key,Sname varchar(25) not null, address varchar(30) not null, mno bigint , Cno int references Course(cno));
insert into Student value(100, "kedar pawar","Talsande",7620374183,1),(99, "Amruta pawar","Talsande",1234567890,1);
insert into student value(10,"Ashish patil", "TAlsande",0987654321,2),(11,"Aditya patil", "TAlsande",0987623321,2);
insert into student value(1,"bruce wayne", "TAlsande",0912654321,3),(2," itachi uchiha", "TAlsande",0911234321,3);
insert into student value(3,"  john wick", "TAlsande",0912654321,4),(4," frank castle", "TAlsande",09112312341,3);
select * from Student;
create table Student_FEES( Recno int primary key,Recdate varchar(30) not null  , Rno int references Student(Rno), Recamt int);

insert into student_fees value
				(4001,"30-10-2023",100,60000),(4002,"28-10-2023",99,25000),
                (4003,"29-10-2023",11,9000),(4004,"27-10-2023",10,33000),
				(4005,"28-10-2023",1,28000),(4006,"28-10-2023",2,20000),
                (4007,"20-10-2023",3,25000),(4008,"28-10-2023",4,29800),
                (4009,"31-10-2023",5,60000),(4010,"1-11-2023",6,60000);
select * from Student_FEES;

DELIMITER $$
CREATE PROCEDURE pro_up(
    IN vrno INT)
BEGIN
        update Student_fees set recamt=10000 where rno=vrno;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE pro_drodel(
    IN vrno INT)
BEGIN
        delete from Student_fees where rno=vrno;
       drop table Student;
END$$
DELIMITER ;

#Creating a user

#You can create the user with the appropriate host and privileges using the following command:
CREATE USER 'Kedar'@'localhost' IDENTIFIED BY '1234567';

SELECT user, host FROM mysql.user WHERE user = 'Kedar';#This will show you the host(s) associated with the 'Kedar' user.

#Syntax: SELECT user, host FROM mysql.user;

#Remember to run these queries with a user account that has the necessary privileges to access the mysql database and user table, such as the MySQL root user.

GRANT ALL PRIVILEGES ON School.* TO 'Kedar'@'localhost';