import mysql.connector #Importing Connector package   
mysqldb=mysql.connector.connect(host="localhost",user="belprofbiz",password="ANANERBE_80224552332")#established connection   
mycursor=mysqldb.cursor()#cursor() method create a cursor object  
mycursor.execute ("USE andrey")
mycursor.execute("create table newtable(id INT, A INT, B INT,  PRIMARY KEY (id))")#Execute SQL Query to create a table into your database

    
mysqldb.close()#Connection Close