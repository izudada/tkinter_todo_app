import sqlite3


conn = sqlite3.connect('todo.db')
print("Opened database successfully")


conn.execute('''CREATE TABLE `todo_info`(  
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   `title` varchar (100) NOT NULL,
   `completed` tinyint ( 1 ) NOT NULL DEFAULT 0
);''')
print("Table todo_info created successfully")
