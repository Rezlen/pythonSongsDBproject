from localMySQL import *

dbCursor.execute("SHOW TABLES")

for tables in dbCursor:
  print(tables)

