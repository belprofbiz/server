import mysql.connector #Importing Connector package   
mysqldb=mysql.connector.connect(host="localhost",user="belprofbiz",password="ANANERBE_80224552332")#established connection   
mycursor=mysqldb.cursor()#cursor() method create a cursor object  
mycursor.execute("create database andrey")#Execute SQL Query to create a database

    
mysqldb.close()#Connection Close