use human_resource;
--Viewing the table structure --

-- Viewing table structures and the data --
select * from hr_1m;
select * from hr_2m;
select * from hr_5m;

--Confirming the number of distinct records in each table--
select count(distinct [Emp ID]) AS '1m' from hr_1m;

select count(distinct [Emp ID]) AS '2m' from hr_2m;
select count(distinct [Emp ID]) AS '5m' from hr_5m;

SELECT 
	DISTINCT CAST([Emp ID] AS int) AS emp_id,
	[Name Prefix] AS prefix,
	CONCAT([First Name], ' ', [Middle Initial], ' ', [Last Name]) AS employee_name,
	[Mother's Name] AS maiden_name,
	Gender AS gender,
	CAST([Date of Birth] as date) AS dob,
	CAST([Time of Birth] as time) AS birth_time,
	--CAST([Age in Yrs ] as decimal(10, 0)) AS age,-- 
	CAST([Weight in Kgs ] as decimal(10, 1)) AS weight_kgs,
	CAST([Date of Joining] as date) AS join_date,
	[Half of Joining] AS half_yr_joined,
	[Quarter of Joining] AS quarter_joined,
	CAST([Month of Joining] as int) AS month_joined,
	[Month Name of Joining] as month_joined_name,
	CAST([Age in Company (Years)] as decimal(10, 2)) AS age_in_company_yrs,	
	CAST([Year of Joining] as int) AS join_year,
	SSN AS ssn,
	[Phone No  ] AS phone,
	[E Mail] AS email,
	[Place Name] place,
	County AS county,
	City AS city,
	State AS state,
	CAST(Zip AS int) AS zipcode,
	Region AS region,
	CAST([Salary] AS decimal(10, 2)) AS salary

from hr_5m;

-- creating well formatted tables
DROP TABLE hr_1m_clean;

SELECT 
	CAST([Emp ID] AS int) AS emp_id,
	[Name Prefix] AS prefix,
	CONCAT([First Name], ' ', [Middle Initial], ' ', [Last Name]) AS employee_name,
	[Mother's Name] AS maiden_name,
	Gender AS gender,
	CAST([Date of Birth] as date) AS dob,
	CAST([Time of Birth] as time) AS birth_time,
	--CAST([Age in Yrs ] as decimal(10, 0)) AS age,-- 
	CAST([Weight in Kgs ] as decimal(10, 1)) AS weight_kgs,
	CAST([Date of Joining] as date) AS join_date,
	[Half of Joining] AS half_yr_joined,
	[Quarter of Joining] AS quarter_joined,
	CAST([Month of Joining] as int) AS month_joined,
	[Month Name of Joining] as month_joined_name,
	CAST([Age in Company (Years)] as decimal(10, 2)) AS age_in_company_yrs,	
	CAST([Year of Joining] as int) AS join_year,
	SSN AS ssn,
	[Phone No  ] AS phone,
	[E Mail] AS email,
	[Place Name] place,
	County AS county,
	City AS city,
	State AS state,
	CAST(Zip AS int) AS zipcode,
	Region AS region,
	CAST([Salary] AS decimal(10, 2)) AS salary
INTO hr_1m_clean
FROM hr_1m 

SELECT 
	CAST([Emp ID] AS int) AS emp_id,
	[Name Prefix] AS prefix,
	CONCAT([First Name], ' ', [Middle Initial], ' ', [Last Name]) AS employee_name,
	[Mother's Name] AS maiden_name,
	Gender AS gender,
	CAST([Date of Birth] as date) AS dob,
	CAST([Time of Birth] as time) AS birth_time,
	--CAST([Age in Yrs ] as decimal(10, 0)) AS age,-- 
	CAST([Weight in Kgs ] as decimal(10, 1)) AS weight_kgs,
	CAST([Date of Joining] as date) AS join_date,
	[Half of Joining] AS half_yr_joined,
	[Quarter of Joining] AS quarter_joined,
	CAST([Month of Joining] as int) AS month_joined,
	[Month Name of Joining] as month_joined_name,
	CAST([Age in Company (Years)] as decimal(10, 2)) AS age_in_company_yrs,	
	CAST([Year of Joining] as int) AS join_year,
	SSN AS ssn,
	[Phone No  ] AS phone,
	[E Mail] AS email,
	[Place Name] place,
	County AS county,
	City AS city,
	State AS state,
	CAST(Zip AS int) AS zipcode,
	Region AS region,
	CAST([Salary] AS decimal(10, 2)) AS salary
INTO hr_5m_clean
FROM hr_5m

SELECT 
	CAST([Emp ID] AS int) AS emp_id,
	[Name Prefix] AS prefix,
	CONCAT([First Name], ' ', [Middle Initial], ' ', [Last Name]) AS employee_name,
	[Mother's Name] AS maiden_name,
	Gender AS gender,
	CAST([Date of Birth] as date) AS dob,
	CAST([Time of Birth] as time) AS birth_time,
	--CAST([Age in Yrs ] as decimal(10, 0)) AS age,-- 
	CAST([Weight in Kgs ] as decimal(10, 1)) AS weight_kgs,
	CAST([Date of Joining] as date) AS join_date,
	[Half of Joining] AS half_yr_joined,
	[Quarter of Joining] AS quarter_joined,
	CAST([Month of Joining] as int) AS month_joined,
	[Month Name of Joining] as month_joined_name,
	CAST([Age in Company (Years)] as decimal(10, 2)) AS age_in_company_yrs,	
	CAST([Year of Joining] as int) AS join_year,
	SSN AS ssn,
	[Phone No  ] AS phone,
	[E Mail] AS email,
	[Place Name] place,
	County AS county,
	City AS city,
	State AS state,
	CAST(Zip AS int) AS zipcode,
	Region AS region,
	CAST([Salary] AS decimal(10, 2)) AS salary
INTO hr_2m_clean
FROM hr_2m

-- Sort the data according the year of joining in decsending order --
SELECT * FROM hr_1m_clean ORDER BY join_year DESC;
SELECT * FROM hr_2m_clean ORDER BY join_year DESC;
SELECT * FROM hr_5m_clean ORDER BY join_year DESC;

-- Determine the number of Employees per state--
SELECT state AS State, COUNT(*) AS "No. of Employees" FROM hr_1m_clean GROUP BY state ORDER BY state;

-- Average age as at today--
SELECT state AS State, AVG(FLOOR(DATEDIFF(DAY, dob, GETDATE()) / 365.25)) AS "Avg Age" FROM hr_2m_clean GROUP by State;

-- Average age per state as at 2020-12-31 --
SELECT state AS State, AVG(FLOOR(DATEDIFF(DAY, dob, '2020-12-31') / 365.25)) AS "Avg Age" FROM hr_1m_clean WHERE dob IS NOT NULL GROUP by State;

-- Find the majority of employees per state grouped by a gender --
SELECT state AS State, gender, COUNT(*) 
FROM hr_1m_clean
GROUP BY state, gender;

-- Which gender forms majority of the workforce --
SELECT Count(*) AS "Workforce per Gender" FROM hr_1m_clean GROUP BY gender ORDER BY gender;

-- Average duration in the company for employees per gender --
SELECT AVG(FLOOR(DATEDIFF(DAY, join_date, '2020-12-31') / 365.25)) AS "Average Duration" FROM hr_1m_clean GROUP BY gender ORDER BY gender; 

-- Creating Views --
-- Age --
drop VIEW employee_age
CREATE VIEW employee_age AS 
	SELECT *, (FLOOR(DATEDIFF(YEAR, dob, '2020-12-31'))) AS emp_age 
	FROM hr_1m_clean
	WHERE dob IS NOT NULL;

select count(*) from employee_age where emp_age between 20 and 30;

create view hr_5m_2m AS
	select * from hr_5m_clean
	INNER JOIN
	hr_2m_clean
	ON hr_5m_clean.emp_id = hr_2m_clean.emp_id;

-- common table expressionsn --
WITH cte_reports AS
(SELECT emp_id, employee_name, gender, dob, join_date, emp_age FROM employee_age
WHERE emp_age BETWEEN 60 AND 70)
SELECT * FROM cte_reports ORDER BY emp_id, gender, join_date;

-- recursive cte function --
WITH consecutive_number_sum(i, consec_sum) AS (
SELECT 0, 0 UNION ALL 
SELECT i + 1, consec_sum + (i + 1)
FROM consecutive_number_sum
where i < 5)
SELECT consec_sum 
FROM consecutive_number_sum
WHERE i = 4

WITH empl_state AS(
SELECT state, gender, count(distinct emp_id) AS 'Total Employees' FROM employee_age group by state, gender
)
SELECT * FROM empl_state;

select * from employee_age