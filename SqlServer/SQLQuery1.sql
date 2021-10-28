/*DDL*/


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


/*Contraints*/
/*not null, unique, check, Default, Index*/


-------------------------------------------------------------------------------------------------------------------------
drop table StudentsInfo;
CREATE TABLE StudentsInfo					
(
StudentId int,								
StudentName varchar(8000) Not null,          -- not null (or) ALTER TABLE  StudentsInfo ALTER COLUMN PhoneNumber Not Null;
PartnerName varchar(8000),
PhoneNumber bigint,
AddressOfStudent varchar(8000),
City varchar(8000),
Country varchar(8000)
);


-------------------------------------------------------------------------------------------------------------------------
drop table StudentsInfo;
CREATE TABLE StudentsInfo					
(
StudentId int,								
StudentName varchar(8000)  ,    
PartnerName varchar(8000),
PhoneNumber bigint,
AddressOfStudent varchar(8000),
City varchar(8000),
Country varchar(8000),
Constraint constraint1 UNIQUE(StudentId,PhoneNumber)  -- adding unique constraints to multiple coulumn
);
-- (or) Alter Table StudentsInfo ADD UNIQUE(sTUDENT_ID)
--To drop constraint
Alter Table studentsInfo Drop Constraint constraint1;  


-------------------------------------------------------------------------------------------------------------------------
-- Check constraints
drop table StudentsInfo;
CREATE TABLE StudentsInfo					
(
StudentId int,								
StudentName varchar(8000)  ,    
PartnerName varchar(8000),
PhoneNumber bigint,
AddressOfStudent varchar(8000),
City varchar(8000),
Country varchar(8000) check (country = 'India') --check constraint
);

-- Alter table table name add constraints checkconstraintname check(country = 'India')





-------------------------------------------------------------------------------------------------------------------------
-- Default constraints
drop table StudentsInfo;
CREATE TABLE StudentsInfo					
(
StudentId int,								
StudentName varchar(8000)  ,    
PartnerName varchar(8000),
PhoneNumber bigint,
AddressOfStudent varchar(8000),
City varchar(8000),
Country varchar(8000) Default 'India'
);

/* 
https://www.youtube.com/watch?v=k0S4P-a6d5w&list=PL08903FB7ACA1C2FB&index=44&t=683s
*/