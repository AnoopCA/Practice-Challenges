5.  Create Database: 
    ○  Write a SQL query to create a new database named CompanyDB.  
		CREATE DATABASE CompanyDB;
		USE CompanyDB;

6.  Create Table: 
    ○  Write a SQL query to create a table named Employees with the following columns:
       EmployeeID (INT, Primary Key), FirstName (VARCHAR(50)), LastName (VARCHAR(50)), Department (VARCHAR(50)), Salary (DECIMAL(10, 2)). 
		CREATE TABLE Employees(EmployeeID INT, FirstName VARCHAR(50), LastName VARCHAR(50), Department VARCHAR(50), Salary DECIMAL(10,2), CONSTRAINT pk_emp_id PRIMARY KEY(EmployeeID));
        
7.  Insert Data: 
    ○  Write a SQL query to insert the following data into the Employees table: 
        EmployeeID  FirstName  LastName  Department  Salary 
        1  John  Doe  HR  50000 
        2  Jane  Smith  IT  60000 
        3  Emily  Johnson  Marketing  55000 
        4  Michael  Brown  IT  70000 
        5  Linda  Davis  HR  48000 
        
		INSERT INTO employees (EmployeeID, FirstName, LastName, Department, Salary) VALUES
        (1, "John", "Doe", "HR" ,50000),
        (2, "Jane", "Smith", "IT", 60000),
        (3, "Emily", "Johnson", "Marketing", 55000),
        (4, "Michael", "Brown", "IT", 70000 ),
        (5, "Linda", "Davis", "HR", 48000);
        
8.  Select Data: 
    ○  Write a SQL query to select all columns from the Employees table.    
		SELECT * FROM employees;
        
9.  Select Specific Columns: 
    ○  Write a SQL query to select only FirstName, LastName, and Department columns from the Employees table. 
		SELECT FirstName, LastName, Department FROM employees;
        
10. WHERE Clause: 
    ○  Write a SQL query to select all employees who work in the IT department.
		SELECT * FROM employees WHERE department="IT";

11. Using AND in WHERE Clause: 
    ○  Write a SQL query to select employees who work in the IT department and have a salary greater than 60000.  
		SELECT * FROM employees WHERE department="IT" AND salary>60000;
        
12. Using OR in WHERE Clause: 
    ○  Write a SQL query to select employees who work in the HR department or have a salary less than 50000. 
		SELECT * FROM employees WHERE department="HR" OR salary<50000;
        
13. ORDER BY Clause: 
    ○  Write a SQL query to select all employees, ordered by LastName in ascending order.  
		SELECT * FROM employees ORDER BY lastname ASC;
        
14. UPDATE Command: 
    ○  Write a SQL query to update the salary of Emily Johnson to 58000. 
		UPDATE employees SET salary=58000 WHERE firstname="Emily" AND lastname="Johnson";
		
15. DELETE Command: 
    ○  Write a SQL query to delete the employee record with EmployeeID equal to 5. 
		DELETE FROM employees WHERE employeeid=5;
        
16. Aggregate Functions: 
    ○  Write a SQL query to calculate the average salary of employees in the IT department.  
		SELECT AVG(salary) AS Average_Salary FROM employees WHERE department="IT";
        
17. GROUP BY Clause: 
    ○  Write a SQL query to find the total salary expense for each department.  
		SELECT department, AVG(salary) AS Average_Salary FROM employees GROUP BY department;

18. HAVING Clause: 
    ○  Write a SQL query to select departments with a total salary expense greater than 100000.  
		SELECT department, SUM(salary) AS Average_Salary FROM employees GROUP BY department HAVING Average_Salary>100000;

19. JOIN Clause: 
    ○  Create another table named Departments with the following columns: DepartmentID (INT, Primary Key), DepartmentName (VARCHAR(50)). 
        Populate it with appropriate data, then write a SQL query to join the Employees and Departments tables and select all columns.  
		
        CREATE TABLE Departments (DepartmentID INT, DepartmentName VARCHAR(50), CONSTRAINT pk_dept_id PRIMARY KEY(DepartmentID));
		INSERT INTO departments (departmentid, departmentname) VALUES (1, "HR"), (2, "IT"), (3, "Marketing");
        SELECT * FROM employees AS E LEFT JOIN departments AS D ON E.department=D.departmentname;
        
20. Subquery: 
    ○  Write a SQL query to find the employee(s) with the highest salary.
		SELECT A.employeeid as EmployeeID, A.firstname AS FirstName, A.department AS Department, A.salary AS Salary FROM
        (SELECT *, RANK() OVER(ORDER BY salary DESC) as salary_rank FROM employees) AS A WHERE A.salary_rank=1;

    