import mysql.connector #Importing Connector package   
mysqldb=mysql.connector.connect(host="localhost",user="belprofbiz",password="ANANERBE_80224552332")#established connection   
mycursor=mysqldb.cursor()#cursor() method create a cursor object  
mycursor.execute ("USE andrey")
mycursor.execute("select * from newtable")#Execute SQL Query to select all record

    
mysqldb.close()#Connection Close