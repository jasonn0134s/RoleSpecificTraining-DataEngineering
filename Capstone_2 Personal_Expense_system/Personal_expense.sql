create database expense_monitor;

use expense_monitor;

create table users (
    user_id int primary key auto_increment,
    user_name varchar(100)
);

create table categories (
    category_id int primary key auto_increment,
    category_name varchar(100)
);

create table expenses (
    expense_id int primary key auto_increment,
    user_id int,
    category_id int,
    amount decimal(10,2),
    expense_date date,
    payment_method varchar(50),

    foreign key (user_id)
    references users(user_id),

    foreign key (category_id)
    references categories(category_id)
);

insert into users(user_name)
values
('Rahul'),
('Priya'),
('Arjun');

insert into categories(category_name)
values
('Food'),
('Travel'),
('Shopping');

insert into expenses(
    user_id,
    category_id,
    amount,
    expense_date,
    payment_method
)
values
(1,1,250,'2026-05-01','UPI'),
(1,2,1200,'2026-05-02','Card'),
(2,3,500,'2026-05-03','Cash'),
(3,1,300,'2026-05-04','UPI');

select * from expenses;

update expenses
set amount = 1500
where expense_id = 2;

delete from expenses
where expense_id = 4;

delimiter //

create procedure monthly_category_expense()
begin

    select
        c.category_name,
        month(e.expense_date) as expense_month,
        sum(e.amount) as total_expense

    from expenses e

    join categories c
    on e.category_id = c.category_id

    group by
        c.category_name,
        month(e.expense_date);

end //

delimiter ;

call monthly_category_expense();