import mysql.connector

conn = mysql.connector.connect(user='root', password='123456')
cursor = conn.cursor()
#cursor.execute("drop database chat")
cursor.execute("create database chat")
cursor.execute("use chat")
cursor.execute('''create table c_blog (
								blog_id int primary key auto_increment, 
								blog_content varchar(150),
								user_id int(10),
								user_name varchar(18),
								thump int default 0,
								pageview int(6) default 0,
								create_at timestamp default current_timestamp, 
								update_at timestamp default current_timestamp on update current_timestamp
						)''')
cursor.execute('''create table c_user (
								user_id int primary key auto_increment, 
								user_name varchar(18),
								passcode varchar(32),
								phone_number varchar(15),
								chat_head blob,
								introduction varchar(60),
								create_at timestamp default current_timestamp, 
								update_at timestamp default current_timestamp on update current_timestamp
						)''')
cursor.execute('''create table c_comment (
								comment_id int(8) primary key , 
								user_id int(8),
								blog_id int(8),
								comment_content varchar(100),
								comment_likes int(8),
								create_at timestamp default current_timestamp, 
								update_at timestamp default current_timestamp on update current_timestamp
						)''')
