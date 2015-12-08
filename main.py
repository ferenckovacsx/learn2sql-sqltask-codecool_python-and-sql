import mysql.connector

#f = open("create.sql",'r')
#f = open("insert.sql",'r')
#f = open("append.sql",'r')
#f = open("modifying.sql",'r')
#f = open("remove.sql",'r')
f = open("query.sql",'r')

out = f.readlines()
f.close()

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='codecool')
cursor = cnx.cursor()
sql = ""
try:
    for i in range(len(out)):
        sql += out[i]
        cursor.execute(out[i])
        data = cursor.fetchall()
        for row in data :
            print(row)
        cnx.commit()
except:
   cnx.rollback()
cnx.close()