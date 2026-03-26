create database company_training;
use company_training;

create table employees (
emp_id int primary key,
emp_name varchar(100),
department varchar(50),
city varchar(50)
);

create table projects (
project_id int primary key,
emp_id int,
project_name varchar(100),
project_budget decimal(12,2),
project_status varchar(50)
);

insert into employees values
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', null),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, null, 'Marketing', 'Chennai');

insert into projects values
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, null, 'Website Revamp', 60000, 'Pending'),
(106, 8, 'Mobile App', 100000, 'Active');


-- exercise 1
select e.emp_name, p.project_name, p.project_budget
from employees e
inner join projects p
on e.emp_id = p.emp_id;


-- exercise 2
select e.emp_name, p.project_name
from employees e
left join projects p
on e.emp_id = p.emp_id;


-- exercise 3
select e.emp_name, p.project_name
from employees e
right join projects p
on e.emp_id = p.emp_id;


-- exercise 4
/* full outer join simulation */
select e.emp_name, p.project_name
from employees e
left join projects p
on e.emp_id = p.emp_id

union

select e.emp_name, p.project_name
from employees e
right join projects p
on e.emp_id = p.emp_id;


-- exercise 5
select e.emp_name, p.project_name
from employees e
cross join projects p;


-- exercise 6
select e.emp_name, p.project_name
from employees e
join projects p
on e.emp_id = p.emp_id
where e.department = 'IT';


-- exercise 7
select e.emp_name, p.project_name, p.project_budget
from employees e
join projects p
on e.emp_id = p.emp_id
where p.project_budget > 100000;


-- exercise 8
select e.emp_name, p.project_name
from employees e
join projects p
on e.emp_id = p.emp_id
where e.city = 'Hyderabad';


-- exercise 9
select e.emp_name, count(p.project_id) as total_projects
from employees e
left join projects p
on e.emp_id = p.emp_id
group by e.emp_name;


-- exercise 10
select e.emp_name, sum(p.project_budget) as total_budget
from employees e
left join projects p
on e.emp_id = p.emp_id
group by e.emp_name;


-- exercise 11
select e.department, avg(p.project_budget) as avg_budget
from employees e
join projects p
on e.emp_id = p.emp_id
group by e.department;


-- exercise 12
select e.department, count(p.project_id) as total_projects
from employees e
left join projects p
on e.emp_id = p.emp_id
group by e.department;


-- exercise 13
select e.department, sum(p.project_budget) as total_budget
from employees e
left join projects p
on e.emp_id = p.emp_id
group by e.department;


-- exercise 14
select city, count(emp_id) as total_employees
from employees
group by city;


-- exercise 15
select e.emp_name, count(p.project_id) as total_projects
from employees e
join projects p
on e.emp_id = p.emp_id
group by e.emp_name
having count(p.project_id) > 1;


-- exercise 16
select e.department, sum(p.project_budget) as total_budget
from employees e
join projects p
on e.emp_id = p.emp_id
group by e.department
having sum(p.project_budget) > 150000;


-- exercise 17
select e.emp_name, sum(p.project_budget) as total_budget
from employees e
join projects p
on e.emp_id = p.emp_id
group by e.emp_name
having sum(p.project_budget) > 100000;


-- exercise 18 capstone query
select 
e.emp_name,
e.department,
sum(p.project_budget) as total_budget
from employees e
join projects p
on e.emp_id = p.emp_id
group by e.emp_name, e.department
having sum(p.project_budget) > 100000
order by total_budget desc;
