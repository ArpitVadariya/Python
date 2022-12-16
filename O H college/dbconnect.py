#this work in python 3.7..
#open cmd as administrator and run this ("pip install mysql-connector-python")
#open xampp control panel and start mysql server 
#and than this code work

import mysql.connector

#for a create database in mysql database
db=mysql.connector.connect(host="localhost",user="root",password="")
cursor=db.cursor()
# query="create database python"
# cursor.execute(query)


#main connection
db1=mysql.connector.connect(host="localhost",user="root",password="",database="python")
cursor=db1.cursor()

#for a create table
# try:
#     tablecreate = cursor.execute("create table Table1(id int(10),name varchar(100),password varchar(100))")
#     print("table created successfully.")
# except:
#     print("kuch to gadbad hai daya🤏.")

# try:
#     cursor.execute("Alter table Table1 add superhero varchar(100) after id")
#     print("navi column nakhi didhi.")
# except:
#     print("kuch to gadbad hai daya🤏.")

# try:
#     cursor.execute("ALTER TABLE table1 MODIFY id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY")
#     print("fari gyu.")
# except:
#     print("kuch to gadbad hai daya🤏.")
    

#for a insert values in table
# try:
#     query="insert into table1(superhero,name) values(%s,%s)"
#     # number = int(input("number = "))
#     superheroname = input("superheroname = ")
#     name = input("name = ")
#     user = [(superheroname, name)]
#     cursor.executemany(query,user)
#     print("data database ma gari gya chhe")
# except:
#     print("kuch to gadbad he daya🤏.")

# for truncate table
# try:
#     cursor.execute("truncate table table1")
#     print("table dhoru thay gyu")
# except:
#     print("kuch to gadbad hai daya🤏.")

#for a fetch data from table
# query="select * from table1"
# cursor.execute(query)
# result=cursor.fetchall()
# for data in result:
#     print(data)



#for update table
    #query="update hitesh set password='hiteshodii' where name='odedara hitesh'"
    #cursor.execute(query)


#for a delete data from table
    #query="delete from hitesh where id=1"
    #cursor.execute(query)


#for a drop table
# query="drop table table1"
# cursor.execute(query)


db1.commit()
# db.commit()
