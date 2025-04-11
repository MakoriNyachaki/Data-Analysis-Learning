create database school;

use school;

create table students(
	student_id int auto_increment primary key,
    last_name varchar(100) not null,
    other_name varchar(250) not null,
    parent_id int not null,
    class_adm int not null,
    dob date not null,
    doa date not null,
    foreign key(parent_id) references parents(id)    
);

create table parents(
	id int primary key not null,
    parent_name varchar(300) not null, 
    phone varchar(20) primary key not null,
    email varchar(200) primary key not null,
    postal_address int null,
    postal_code int null,
    town varchar(100) not null
);

create table subjects(
	id int primary key auto_increment not null,
    sub_code varchar(6) primary key not null,
    sub_name varchar(50) unique not null
);
