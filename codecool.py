import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='codecool')
cursor = cnx.cursor()
sql = "INSERT INTO `codecool`.`users` (`Id`, `Name`, `Birthdate`, `Introduction`, `Avatar`, `Email`) VALUES (NULL, 'MateGG', '2015-12-08 00:00:00', 'asddaasd', 'nincs', 'gg@gg.hu');"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   cnx.commit()
except:
   # Rollback in case there is any error
   cnx.rollback()
cnx.close()