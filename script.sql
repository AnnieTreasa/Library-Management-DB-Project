create database library;
use library;
create table user(
	user_id varchar(100) not null primary key,
    name varchar(100) not null,
    ph_no varchar(10) not null,
    password varchar(6) not null,
    dept varchar(100) not null,
    admin_year year not null
    
);
create table book(
	book_id int not null primary key,
    book_name varchar(100) not null,
    publisher varchar(100) not null,
    author varchar(100) not null,
    publish_date date not null,
    status enum("issued","not issued") default "not issued"


    
);
insert into book (book_id,book_name,publisher,author,publish_date)values
(3,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(1,"Wings of fire","DC books","Abdul Kalam","2022-9-2"),
(2,"Wings of fire","DC books","Abdul Kalam","2001-9-2"),
(4,"Wings of fire","DC books","Abdul Kalam","2001-9-2"),
(5,"Wings of fire","DC books","Abdul Kalam","2001-9-2"),
(6,"Diary of a young girl","DC books","Anne Frank","2001-9-2"),
(7,"Wings of fire","DC books","Abdul Kalam","2001-9-2"),
(8,"Wings of fire","DC books","Abdul Kalam","2001-9-2"),
(9,"Wings of fire","DC books","Abdul Kalam","2001-9-2"),
(10,"Wings of fire","DC books","Abdul Kalam","2001-9-2"),
(11,"Diary of a young girl","DC books","Anne Frank","2022-10-8"),
(12,"Diary of a young girl","DC books","Anne Frank","2000-10-8"),
(13,"Diary of a young girl","MN books","Anne Frank","1980-10-8"),
(14,"Diary of a young girl","DC books","Anne Frank","1980-10-8"),
(15,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(16,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(17,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(18,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(19,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(20,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(21,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(22,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(23,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(24,"Diary of a young girl","DC books","Anne Frank","1981-5-8"),
(25,"Diary of a young girl","DC books","Anne Frank","1981-5-8");
 
 create table Borrowed(
	book_id int not null,
    user_id varchar(100) not null,
    issue_date date not null,
    foreign key(book_id) references book(book_id) on delete cascade,
    foreign key(user_id) references user(user_id) on delete cascade
    
 );
 
 
 


