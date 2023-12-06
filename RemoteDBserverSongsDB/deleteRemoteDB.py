
from mainRemoteDB import *

"""
try:
  # droping a table
  dbCursor.execute("DROP TABLE downloads")
  dbCursor.execute("ALTER TABLE downloads ADD FOREIGN KEY (SongID) REFERENCES songs(SongID)")

  print("Tables by deleteRemoteDB.py created successfully")

except MySQLdb.Error as e:
  print("Error deleting tables:", e)

finally:
  connection.close()

"""
# create subroutine
def delete_songs():
  try:
    # use primary key to delete a record 
    idField = input("Enter the SongID of the record to be deleted: ")
    # DELETE FROM songs WHERE SongID = 1/2/3/4/5/.....
    dbCursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
    connection.commit()

    print(f"Record '{idField}' deleted from songs table ")
  
  except MySQLdb.Error as e:
    print(f"Error updating/adding record: {e}")

if __name__ == "__main__":
  delete_songs()
  
