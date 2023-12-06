from connect import *

# create subroutine 
def delete_songs():

  # use primary key to delete a record 
  idField = input("Enter the SongID of the record to be deleted: ")


  # DELETE FROM songs WHERE SongID = 1/2/3/4/5/.....
  dbCursor.execute(f"DELETE FROM songs WHERE SongID = {idField}")
  dbCon.commit()

  print(f"Record {idField} deleted from songs table ")

if __name__ == "__main__":
  delete_songs()