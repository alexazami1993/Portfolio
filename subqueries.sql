-- subquery in select
SELECT * FROM salaries

select emp_no, salary, (select avg(salary) from salaries) as AllAverageSalary
FROM salaries

-- how to do it with Partition By
SELECT emp_no, salary, avg(salary) over () as AllAvgSalary
FROM salaries
Group By emp_no, salary
order by 1,2

-- subquery in from
SELECT a.emp_no, AllAvgSalary
FROM (select emp_no, salary, avg(salary) over () as AllAvgSalary
from salaries) a

-- subquery in where
select emp_no,title
FROM titles WHERE emp_no IN (select emp_no from salaries WHERE emp_no BETWEEN '1001' AND '1009')