#creating company database

create database  company_db;
use  company_db;

# make it as default shema
create table employee(
	fname varchar(30),
	minit char(1),
	lname varchar(30),
	ssn char(9),
	bdate date,
	address varchar(30),
	sex char(1),
	salary float(10,2),
	super_ssn char(9),
	dno smallint(6),
	constraint pk_employee PRIMARY KEY (ssn)
);

create table department(
	dname varchar(30),
	dnumber smallint,
	mgr_ssn char(9),
	mgr_start_date date,
	constraint pk_department PRIMARY KEY (dnumber)
);

create table dept_locations(
	dnumber smallint,
	dlocation varchar(20),
	constraint pk_dept_loc PRIMARY KEY (dnumber,dlocation)
);

create table project(
	pname varchar(30),
	pnumber smallint,
	plocation varchar(30),
	dnum smallint,
	constraint pk_project PRIMARY KEY (pnumber)
);

create table works_on(
	essn char(9),
	pno smallint,
	hours float(4,2),
	constraint pk_works_on PRIMARY KEY (essn, pno)
);

create table dependent(
	essn char(9),
	dependent_name varchar(30),
	sex char(1),
	bdate date,
	relationship varchar(20),
	constraint pk_dependent PRIMARY KEY (essn, dependent_name)
);


insert into employee(fname,minit,lname,ssn,bdate,address,sex,salary,super_ssn,dno) VALUES
('John','B','Smith','123456789','1965-01-09','731 Fondren, Houston, TX','M',30000,'333445555',5),
('Franklin','T','Wong','333445555','1955-01-09','638 Fondren, Houston, TX','M',40000,'888665555',5),
('Alicia','J','Zelaya','999887777','1968-01-09','3321 Fondren, Houston, TX','F',25000,'987654321',4),
('Jennifer','S','Wallace','987654321','1941-01-09','21 Fondren, Houston, TX','F',43000,'888665555',4),
('Ramesh','K','Narayan','666884444','1962-01-09','975 Fondren, Houston, TX','M',38000,'333445555',5),
('Joyce','A','English','453453453','1972-01-09','5631 Fondren, Houston, TX','F',25000,'333445555',5),
('Ahmad','V','Jabbar','987987987','1969-01-09','980 Fondren, Houston, TX','M',25000,'987654321',4),
('James','E','Borg','888665555','1937-01-09','450 Fondren, Houston, TX','M',55000,NULL,1);

insert into department(dname,dnumber,mgr_ssn,mgr_start_date) VALUES
('Research',5,333445555,'1988-05-22'),
('Administration',4,987654321,'1995-05-22'),
('Headquarters',1,888665555,'1981-05-22');

insert into dept_locations(dnumber,dlocation) values
(1, 'Houston'),
(4, 'Stafford'),
(5, 'Bellaire'),
(5, 'Sugarland'),
(5, 'Houston');

insert into works_on (essn, pno, hours) values
('123456789', 1, 32.5),
('123456789', 2, 7.5),
('666884444', 3, 40.0),
('453453453', 1, 20.0),
('453453453', 2, 20.0),
('333445555', 2, 10.0),
('333445555', 3, 10.0),
('333445555', 10, 10.0),
('333445555', 20, 10.0),
('999887777', 30, 30.0),
('999887777', 10, 10.0),
('987987987', 10, 35.0),
('987987987', 30, 5.0),
('987654321', 30, 20.0),
('987654321', 20, 15.0),
('888665555', 20, NULL);

insert into project(pname,pnumber,plocation,dnum) values
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 4);

insert into dependent(essn,dependent_name,sex,bdate,relationship) values
('333445555', 'Alice', 'F', '1986-04-05', 'Daughter'),
('333445555', 'Theodore', 'M', '1983-04-05', 'Son'),
('333445555', 'Joy', 'F', '1958-04-05', 'Spouse'),
('987654321', 'Abner', 'M', '1942-04-05', 'Spouse'),
('123456789', 'Michael', 'M', '1988-04-05', 'Son'),
('123456789', 'Alice', 'M', '1988-04-05', 'Daughter'),
('123456789', 'Elizabeth', 'M', '1967-04-05', 'Spouse');


#------------------------------------------------------------------------------------------------------------------------------

# employee - fname, minit, lname, ssn,bdate, address, sex,salary, super_ssn, dno
# department - dname, dnumber, mgr_ssn, mgr_start_date
# dept_locations - dnumber, dlocation
# works_on - essn, pno, hours
# project - pname, pnumber, plocation, dnum
# dependent - essn, dependent_name, sex, bdate, relationship

SELECT * FROM employee WHERE dno=5 AND sex="M";
SELECT * FROM employee WHERE dno=5 OR sex="M";
SELECT fname AS "First Name", lname AS "Last Name", ssn, salary, sex FROM employee WHERE salary<=45000 AND sex="M";
SELECT * FROM works_on where hours>15;
SELECT essn, relationship FROM dependent WHERE relationship="Daughter";
SELECT pname AS Project_Name, pnumber AS Project_Number, plocation FROM project WHERE pnumber>10;
SELECT * FROM employee WHERE fname LIKE "a%";
SELECT * FROM employee WHERE fname LIKE "%a";
SELECT * FROM employee WHERE fname LIKE "%a%" OR dno = 5;
SELECT * FROM employee WHERE dno!=5;
SELECT * FROM employee WHERE dno<>5;
SELECT * FROM employee WHERE NOT dno=5;
SELECT fname, lname, ssn, sex, dno FROM employee WHERE NOT sex="F" AND dno IN (1,4);
SELECT fname, lname, ssn, sex, dno FROM employee WHERE sex!="F" AND (dno=1 OR dno=4);
SELECT * FROM employee WHERE salary>=30000 AND salary<=40000;
SELECT * FROM employee WHERE salary BETWEEN 30000 AND 40000;
SELECT * FROM employee WHERE dno IN (1,4,5);
SELECT * FROM employee WHERE dno NOT IN (1,5);
SELECT * FROM works_on WHERE hours>=10 AND pno BETWEEN 3 AND 10;
SELECT * FROM dept_locations WHERE dlocation LIKE "%s%";
SELECT * FROM dependent WHERE sex="M" OR relationship IN ("son", "spouse");
SELECT * FROM employee WHERE super_ssn IS NULL;
SELECT * FROM works_on WHERE hours IS NULL;
SELECT * FROM employee ORDER BY salary ASC;
SELECT * FROM employee WHERE salary>30000 AND dno IN (1,4) ORDER BY salary ASC;
SELECT pno, hours FROM works_on WHERE hours IS NOT NULL AND pno<5 ORDER BY hours DESC;
SELECT COUNT(*) AS Total_Rows FROM employee;
SELECT COUNT(*) AS Total_Rows FROM dependent;
SELECT DISTINCT dname FROM department;
SELECT DISTINCT relationship FROM dependent;
SELECT DISTINCT pno FROM works_on;
SELECT DISTINCT dno FROM employee;
SELECT MIN(salary) AS Mininum_Salary, MAX(salary) AS Maximum_Salary FROM employee;
SELECT MIN(hours) AS Minimum_Hours, MAX(hours) AS Maximum_Hours FROM works_on;
SELECT MIN(salary) AS Minimum_Salary FROM employee WHERE dno=5;
SELECT dno, MIN(salary) FROM employee GROUP BY dno;
SELECT dno, COUNT(*) FROM employee GROUP BY dno;
SELECT COUNT(*) AS Employee_Count FROM employee WHERE salary>35000;
SELECT relationship, COUNT(*) AS Number_of_Employees FROM dependent GROUP BY relationship;
SELECT pno AS Project_Number, SUM(hours) AS Total_Project_Hours FROM works_on GROUP BY pno;
SELECT dno, sex, SUM(salary) AS Total_Salary FROM employee GROUP BY dno, sex;
SELECT sex, AVG(salary) AS Average_Salary FROM employee GROUP BY sex;
SELECT dno, COUNT(*) AS Total_Employees, SUM(salary) AS Total_Salary FROM employee GROUP BY dno;
SELECT dno, COUNT(*) AS Total_Employees, SUM(salary) AS Total_Salary FROM employee GROUP BY dno HAVING Total_Employees>=2;
SELECT dno, COUNT(*) AS Total_Employees, SUM(salary) AS Total_Salary FROM employee WHERE sex="M" GROUP BY dno HAVING COUNT(*)>=2;
SELECT dno, AVG(salary) AS Average_Salary FROM employee WHERE sex="M" GROUP BY dno HAVING Average_Salary>35000 ORDER BY Average_Salary ASC;
SELECT *, CASE WHEN sex="M" THEN "Male" WHEN sex="F" THEN "Female" END AS Gender FROM employee;
SELECT *, CASE WHEN salary<30000 THEN "Min Salary" WHEN salary BETWEEN 30000 AND 40000 THEN "Mid Salary" WHEN salary>40000 THEN "Max Salary" END AS Salary_Bucket FROM employee;
SELECT *, CASE WHEN sex="M" THEN salary END AS Male_Salary, CASE WHEN sex="F" THEN salary END AS Female_Salary FROM employee;
SELECT dno, AVG(salary) AS Avg_Salary, AVG(CASE WHEN sex="M" THEN salary END) AS Male_Salary_Avg, AVG(CASE WHEN sex="F" THEN salary END) AS Female_Salary_Avg FROM employee GROUP BY dno;
SELECT *, CASE WHEN salary<30000 THEN "<30k" WHEN salary BETWEEN 30000 AND 40000 THEN "30k - 40k" ELSE ">40k" END AS Salary_Bucket FROM employee;
SELECT essn, COUNT(CASE WHEN relationship="Daughter" THEN 1 END) AS Count_of_Daughters, 
			 COUNT(CASE WHEN relationship="Son" THEN 1 END) AS Count_of_Sons, 
             COUNT(CASE WHEN relationship="Spouse" THEN 1 END) AS Count_of_Spouse FROM dependent GROUP BY essn;
SELECT fname, lname, salary, LAG(salary) OVER(ORDER BY salary ASC) AS Lag_Salary FROM employee;
SELECT fname, lname, salary, LAG(fname) OVER(ORDER BY fname ASC) FROM employee;
SELECT fname, lname, salary, LAG(salary) OVER(ORDER BY salary ASC) AS Lag_Salary, LAG(fname) OVER(ORDER BY salary ASC) AS Lag_fname FROM employee;
SELECT fname, lname, salary, LAG(salary) OVER(ORDER BY fname ASC) AS Lag_Salary, LAG(fname) OVER(ORDER BY fname ASC) AS Lag_fname FROM employee;
SELECT fname, lname, salary, LAG(salary) OVER(ORDER BY salary ASC) as Lag_Salary, LEAD(salary) OVER(ORDER BY salary ASC) AS Lead_Salary FROM employee;
SELECT fname, lname, salary, LAG(salary, 2) OVER(ORDER BY salary DESC) AS Lag_Salary FROM employee;
SELECT fname, lname, salary, LEAD(salary,4) OVER(ORDER BY salary DESC) AS Lead_Salary FROM employee;
SELECT fname, lname, salary, ROW_NUMBER() OVER(ORDER BY fname ASC) as Row_Num FROM employee;
SELECT fname, lname, salary, ROW_NUMBER() OVER(ORDER BY salary ASC) as Row_Num FROM employee;
SELECT fname, lname, salary, RANK() OVER(ORDER BY salary ASC) AS Salary_Rank FROM employee;
SELECT fname, lname, salary, DENSE_RANK() OVER(ORDER BY salary ASC) AS Salary_Dense_Rank FROM employee;
SELECT dno, fname, lname, salary, RANK() OVER(PARTITION BY dno ORDER BY salary DESC) AS Salary_Rank FROM employee;
SELECT *, RANK() OVER(ORDER BY hours DESC) AS Rank_by_Hours FROM works_on;
SELECT *, RANK() OVER(PARTITION BY pno ORDER BY hours DESC) AS Hours_Rank FROM employee;
SELECT * FROM employee E JOIN department D ON E.dno=D.dnumber;
SELECT fname F, lname L, salary FROM employee;
SELECT fname AS F, lname AS L, salary FROM employee;
SELECT E.*, D.dname FROM employee AS E JOIN department AS D ON E.dno=D.dnumber;
SELECT W.essn, E.fname, E.lname, W.pno, W.hours FROM works_on AS W LEFT JOIN employee AS E ON W.essn=E.ssn;
SELECT P.*, D.mgr_ssn AS Dept_Manager_ID FROM project AS P LEFT JOIN department AS D ON P.dnum=D.dnumber;
SELECT P.*, D.mgr_ssn, E.fname, E.lname FROM project AS P LEFT JOIN department AS D ON P.dnum=D.dnumber LEFT JOIN employee AS E ON D.mgr_ssn=E.ssn;
SELECT E.fname, E.lname, W.essn,     W.hours 				 FROM employee AS E LEFT JOIN works_on AS W ON E.ssn=W.essn;
SELECT E.fname, E.lname, W.essn, SUM(W.hours) AS Total_Hours FROM employee AS E LEFT JOIN works_on AS W ON E.ssn=W.essn GROUP BY E.fname, E.lname, W.essn;
SELECT E.fname, E.lname, W.essn, SUM(W.hours) AS Total_Hours FROM employee AS E LEFT JOIN works_on AS W ON E.ssn=W.essn GROUP BY 1,2,3 ORDER BY Total_Hours DESC;
SELECT E.fname, E.lname, E.ssn, COUNT(D.relationship) AS Num_of_Dependents FROM employee AS E LEFT JOIN dependent AS D ON E.ssn=D.essn GROUP BY 1,2,3;
SELECT E.ssn, COUNT(D.relationship) AS Num_Dependents FROM employee AS E RIGHT JOIN dependent AS D ON E.ssn=D.essn GROUP BY E.ssn;
SELECT E.ssn, COUNT(D.relationship) AS Num_Dependents, SUM(W.hours) AS Total_Hours FROM employee AS E LEFT JOIN dependent AS D ON E.ssn=D.essn LEFT JOIN works_on AS W ON E.ssn=W.essn GROUP BY 1;
WITH new_table AS (SELECT E.ssn, COUNT(D.relationship) AS Num_Dependents FROM employee AS E RIGHT JOIN dependent AS D ON E.ssn=D.essn GROUP BY E.ssn)
	SELECT * FROM new_table WHERE Num_Dependents>0; # Common Table Expression - CTE, temporary table is created using "WITH" keyword
WITH new_table_1 AS (SELECT E.ssn AS emp_id, COUNT(D.relationship) AS Num_Dependents FROM employee AS E LEFT JOIN dependent AS D ON E.ssn=D.essn GROUP BY E.ssn),
	 new_table_2 AS (SELECT N.emp_id, N.Num_Dependents, SUM(W.hours) AS Sum_Hours FROM new_table_1 AS N JOIN works_on AS W ON N.emp_id=W.essn GROUP BY 1,2)
     SELECT *, DENSE_RANK() OVER(ORDER BY N2.Sum_Hours DESC) FROM new_table_2 AS N2;
WITH new_table_1 AS (SELECT E.ssn AS emp_id, COUNT(D.relationship) AS Num_Dependents FROM employee AS E LEFT JOIN dependent AS D ON E.ssn=D.essn GROUP BY E.ssn),
	 new_table_2 AS (SELECT N1.emp_id, N1.Num_Dependents, SUM(W.hours) AS Sum_Hours FROM new_table_1 AS N1 JOIN works_on AS W ON N1.emp_id=W.essn GROUP BY 1,2),
     new_table_3 AS (SELECT *, DENSE_RANK() OVER(ORDER BY N2.Sum_Hours DESC) AS Hours_Rank FROM new_table_2 AS N2)
     SELECT * FROM new_table_3 AS N3 WHERE Hours_Rank>=2;
SELECT X.emp_id, X.Num_Dependents, SUM(W.hours) AS Total_Hours FROM
	(SELECT E.ssn AS emp_id, COUNT(D.relationship) AS Num_Dependents FROM employee AS E JOIN dependent AS D ON E.ssn=D.essn GROUP BY E.ssn) AS X 
    JOIN works_on AS W ON X.emp_id=W.essn GROUP BY 1,2;
SELECT * FROM (SELECT *, DENSE_RANK() OVER(ORDER BY Y.Total_Hours DESC) AS Hours_Rank FROM 
	(SELECT X.emp_id, X.Num_Dependents, SUM(W.hours) AS Total_Hours FROM
	(SELECT E.ssn AS emp_id, COUNT(D.relationship) AS Num_Dependents FROM employee AS E LEFT JOIN dependent AS D ON E.ssn=D.essn GROUP BY E.ssn) AS X 
    JOIN works_on AS W ON X.emp_id=W.essn GROUP BY 1,2) AS Y) AS Z WHERE Z.Hours_Rank<=2;
SELECT D.dname, AVG(E.salary) AS Average_Salary FROM department AS D LEFT JOIN employee AS E ON D.dnumber=E.dno GROUP BY D.dnumber;
SELECT X.ssn, X.fname, X.lname, X.dno, Y.Dept_Avg_Salary FROM
	(SELECT ssn, fname, lname, dno FROM employee) AS X
	LEFT JOIN (SELECT dno, AVG(salary) AS Dept_Avg_Salary FROM employee GROUP BY dno) AS Y ON X.dno=Y.dno;
SELECT Z.ssn, Z.fname, Z.lname, Z.dno, Z.avg_salary, Z.super_ssn, E.salary FROM
	(SELECT X.ssn, X.fname AS fname, X.lname AS lname, X.dno AS dno, X.super_ssn AS super_ssn, Y.Avg_Salary AS avg_salary FROM
	(SELECT ssn, fname, lname, dno, super_ssn FROM employee) AS X
    LEFT JOIN (SELECT dno, AVG(salary) AS Avg_Salary FROM employee GROUP BY dno) AS Y ON X.dno=Y.dno) AS Z
    LEFT JOIN employee AS E ON Z.super_ssn=E.ssn ORDER BY Z.super_ssn;
SELECT A.fname, A.lname, A.salary, A.ssn, A.dno, A.super_ssn, E.salary FROM
	(SELECT fname, lname, salary, ssn, dno, super_ssn FROM employee) AS A LEFT JOIN employee E ON A.super_ssn=E.ssn ORDER BY A.super_ssn ASC;
ALTER TABLE employee CHANGE first_name fname VARCHAR(30);
ALTER TABLE employee CHANGE lname last_name VARCHAR(25);
SET SQL_SAFE_UPDATES = 0;
UPDATE employee SET salary=salary*1.1;
UPDATE employee SET salary=salary*0.9 WHERE dno=5;
ALTER TABLE employee ADD bonus INT;
UPDATE employee SET bonus=salary*0.15;
ALTER TABLE employee DROP COLUMN bonus;
ALTER TABLE employee MODIFY first_name VARCHAR(40);
DESCRIBE TABLE employee;
ALTER TABLE employee RENAME TO employee_temp;
ALTER TABLE employee_temp RENAME TO employee;
SELECT ssn, fname, bdate, CURRENT_DATE() as todays_date FROM employee;
SELECT ssn, fname, bdate, CURRENT_TIME() as currenttime FROM employee;
SELECT ssn, fname, bdate, CURRENT_TIMESTAMP() as currenttimestamp FROM employee;
SELECT ssn, fname, bdate, ROUND(DATEDIFF(CURRENT_DATE, bdate)/365.25,0) AS age FROM employee;
SELECT ssn, fname, bdate, YEAR(bdate) AS birthyear, MONTH(bdate) AS birthmonth, DAY(bdate) AS birthday FROM employee;
SELECT ssn, fname, lname, salary FROM employee WHERE ssn IN (SELECT DISTINCT essn FROM dependent); - # Sub query, takes more memory than JOIN

use company_db;
# employee - fname, minit, lname, ssn,bdate, address, sex,salary, super_ssn, dno
# department - dname, dnumber, mgr_ssn, mgr_start_date
# dept_locations - dnumber, dlocation
# works_on - essn, pno, hours
# project - pname, pnumber, plocation, dnum
# dependent - essn, dependent_name, sex, bdate, relationship


# Stored Procedures (Delimiter set to "//" and hence ";" is not considred as the end of the procedure).
DELIMITER //
CREATE PROCEDURE pull_emp_data()
BEGIN
	SELECT * FROM employee ORDER BY salary;
END //
CALL pull_emp_data();
DROP PROCEDURE IF EXISTS pull_emp_data;

DELIMITER //
CREATE PROCEDURE pull_emp(IN emp_id INT)
BEGIN
	SELECT * FROM employee WHERE ssn=emp_id;
END//
CALL pull_emp(123456789);

DROP PROCEDURE IF EXISTS update_salary;
DELIMITER //
CREATE PROCEDURE update_salary(IN emp_id INT, IN new_salary FLOAT)
BEGIN
	UPDATE employee SET salary=new_salary WHERE ssn=emp_id;
	SELECT * FROM employee WHERE ssn=emp_id;
END//
CALL update_salary(123456789, 17000);

DROP PROCEDURE IF EXISTS get_salary;
DELIMITER //
CREATE PROCEDURE get_salary(IN emp_id INT, OUT emp_salary FLOAT)
BEGIN
	SELECT salary INTO emp_salary FROM employee WHERE ssn=emp_id;
END //
CALL get_salary(123456789, @emp_sal);
SELECT @emp_sal AS emp_sal;













