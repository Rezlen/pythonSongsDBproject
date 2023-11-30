
# connecting to databse https://app.planetscale.com/soheilyreza/portfoliowebsite/connect
# Load environment variables from the .env file
# from dotenv import load_dotenv
# load_dotenv()
# import os
# import MySQLdb

# Connect to the database
# connection = MySQLdb.connect(
#   host=os.getenv("aws.connect.psdb.cloud"),
#   user=os.getenv("kqppw0knmqo57dq66i0h"),
#   passwd=os.getenv("pscale_pw_9AVjqamDVhw4IhO2qrpkyLMU7NKHANJLu4Dtdyh38A"),
#   db=os.getenv("portfoliowebsite"),
#   autocommit=True,
#   ssl_mode="VERIFY_IDENTITY",
#   # See https://planetscale.com/docs/concepts/secure-connections#ca-root-configuration
#   # to determine the path to your operating systems certificate file.
#   ssl={ "ca": "" }
# )



# from connect import * # import the connect.py module 
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

connection = MySQLdb.connect(
  host= os.getenv("DB_HOST"),
  user=os.getenv("DB_USERNAME"),
  passwd= os.getenv("DB_PASSWORD"),
  db= os.getenv("DB_NAME"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "MYSQL_ATTR_SSL_CA"
  }
)
  

try:
    # Create a cursor to interact with the database
    cursor = connection.cursor()

    # Execute "SHOW TABLES" query
    cursor.execute("SHOW TABLES")

    # Fetch all the rows
    tables = cursor.fetchall()

    # Print out the tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

except MySQLdb.Error as e:
    print("MySQL Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    