CREATE DATABASE STUDENTS123;			    /*Create a database*/
USE STUDENTS123;							/*Use database students123*/
CREATE TABLE StudentsInfo					/*Create Table*/
(
StudentId int,								
StudentName varchar(8000),
PartnerName varchar(8000),
PhoneNumber bigint,
AddressOfStudent varchar(8000),
City varchar(8000),
Country varchar(8000)
);

/*we cant drop a database that is in use. we can use a different database and drop this database*/
/*as we are using students123 currently we will first switch to students database*/

USE Students;
DROP TABLE StudentsInfo;
DROP DATABASE STUDENTS123;


ALTER TABLE StudentsInfo ADD BloodGroup varchar(8000);          /*Add a Column to a Table*/
ALTER TABLE StudentsInfo DROP COLUMN BloodGroup ;				/*Drop a column*/

ALTER TABLE StudentsInfo ADD DOB DATE;                          /* Table add column */
ALTER TABLE StudentsInfo ALTER COLUMN DOB DATETIME;             /* Tables column change datatype */
ALTER TABLE StudentsInfo DROP COLUMN DOB;						/* Drop column */

INSERT INTO StudentsInfo VALUES('1','VISHU','REDDY','546486463','HEADINGLY','LEADS','UK');     /*Insert into students*/

TRUNCATE TABLE StudentsInfo;								   /*remove values from the table*/

sp_rename 'StudentsInfo', 'InfoStudents';                      /*Rename a Table*/
