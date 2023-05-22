sudo apt install postgresql postgresql-contrib
sudo -i -u postgres
psql

CREATE DATABASE mtuci_db;
CREATE TABLE student_group(id SERIAL PRIMARY KEY,numb varchar NOT NULL, chairvarchar NOT NULL);

/c mtuci_db
select * from students;
select * from student_group;
select * from department;
