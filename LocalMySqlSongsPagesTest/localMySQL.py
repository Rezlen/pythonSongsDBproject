import MySQLdb
# import mysql.connector
 
connection = MySQLdb.connect(
  host="localhost",
  user="root",
  passwd="#######",
  db="dfe2"
)
 
dbCursor = connection.cursor()

# if dbCursor:
#   print("You're connected to database: ")
# else:
#   print('Not connected.')

