create database capstone_sql;
use capstone_sql;

create table students (
student_id int primary key,
student_name varchar(100),
city varchar(50),
age int
);

create table enrollments (
enrollment_id int primary key,
student_id int,
course_name varchar(100),
trainer varchar(100),
fee decimal(10,2)
);

insert into students values
(1,'Aarav Sharma','Hyderabad',22),
(2,'Priya Reddy','Bangalore',23),
(3,'Rahul Verma','Mumbai',24),
(4,'Sneha Kapoor',null,21),
(5,'Vikram Singh','Chennai',25),
(6,null,'Delhi',22);

insert into enrollments values
(101,1,'MySQL','Abdullah Khan',5000),
(102,1,'Python','Abdullah Khan',7000),
(103,2,'Power BI','Kiran',6000),
(104,3,'Azure Data Factory','Sneha',8000),
(105,null,'Excel','Rohan',3000),
(106,8,'Databricks','Ananya',9000);

-- exercise 1
select s.student_name, e.course_name
from students s
inner join enrollments e
on s.student_id = e.student_id;


-- exercise 2
select s.student_name, e.course_name
from students s
left join enrollments e
on s.student_id = e.student_id;


-- exercise 3
select s.student_name, e.course_name
from students s
right join enrollments e
on s.student_id = e.student_id;


-- exercise 4
/* full outer join simulation */
select s.student_name, e.course_name
from students s
left join enrollments e
on s.student_id = e.student_id

union

select s.student_name, e.course_name
from students s
right join enrollments e
on s.student_id = e.student_id;


-- exercise 5
select s.student_name, e.course_name
from students s
cross join enrollments e;


-- exercise 6
select s.student_name, e.course_name
from students s
join enrollments e
on s.student_id = e.student_id
where s.city = 'Hyderabad';


-- exercise 7
select course_name, fee
from enrollments
where fee > 6000;


-- exercise 8
select s.student_name, count(e.course_name) as total_courses
from students s
left join enrollments e
on s.student_id = e.student_id
group by s.student_name;


-- exercise 9
select s.student_name, sum(e.fee) as total_fee_paid
from students s
left join enrollments e
on s.student_id = e.student_id
group by s.student_name;


-- exercise 10
select s.student_name, count(e.course_name) as total_courses
from students s
join enrollments e
on s.student_id = e.student_id
group by s.student_name
having count(e.course_name) > 1;


-- exercise 11
select trainer, sum(fee) as total_fee_collected
from enrollments
group by trainer
having sum(fee) > 10000;


-- exercise 12
SELECT city, COUNT(student_id) AS total_students
FROM students
GROUP BY city
HAVING COUNT(student_id) > 1;

-- final capstone query
select 
s.student_name,
s.city,
sum(e.fee) as total_fee_paid
from students s
join enrollments e
on s.student_id = e.student_id
group by s.student_name, s.city
having sum(e.fee) > 5000
order by total_fee_paid desc;

