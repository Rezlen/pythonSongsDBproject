
# connecting to databse https://app.planetscale.com/soheilyreza/portfoliowebsite/connect
# Load environment variables from the .env file
# from connect import * # import the connect.py module 
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb
# import mysql.connector

connection = MySQLdb.connect(
  host= os.getenv("DATABASE_HOST"),
  user=os.getenv("DATABASE_USERNAME"),
  passwd= os.getenv("DATABASE_PASSWORD"),
  db= os.getenv("DATABASE"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "./cacert.pem"
  }
)


# create a cursor object/variable and assign it to the CURSOR method to run
dbCursor = connection.cursor()
 
# when you have  quotation inside the variable or EXECUTE, it does not count it as comments; it is actual code. 3 quotation quote is for displaying multi lines

try:
  # Create a cursor to interact with the database
  dbCursor = connection.cursor()

  # Execute "SHOW TABLES" query
  dbCursor.execute("SHOW TABLES")

  # Fetch all the rows
  tables = dbCursor.fetchall()

  # Print out the tables
  print("Tables in the database:")
  for table in tables:
    print(table[0])

except MySQLdb.Error as e:
  print("MySQL Error:", e)

finally:
  # Close the cursor and connection
  # dbCursor.close()
  # connection.close()
  print("The Main file run done")
