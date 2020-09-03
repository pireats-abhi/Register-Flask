# Database query
```
create database lecture;

use lecture;

create table registrants(
    id integer not null auto_increment,
    name varchar(255),
    email varchar(255),
    primary key(id)
);

insert into registrants (name, email) values ('abhi', 'adas@gamil.com');

select * from registrants;
```
