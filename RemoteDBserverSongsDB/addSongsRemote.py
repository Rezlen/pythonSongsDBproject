from mainRemoteDB import *

"""
try:
  # adding songs to a table
  dbCursor.execute(
    "insert into songs (Title, Artist, Genre) values ('1984', 'John Smith', 'comedy');"
    "insert into songs (Title, Artist, Genre) values ('The Catcher in the Rye', 'David Thompson', 'adventure');"
  )
  
  # dbCursor.execute("SELECT * FROM songs")
  # dbCursor.execute("ALTER TABLE downloads ADD FOREIGN KEY (SongID) REFERENCES songs(SongID)")
  print("Tables by addSongsRemoteDB.py created successfully")

except MySQLdb.Error as e:
  print("Error deleting tables:", e)
  
  # commit must be just before closing the connection 
  connection.commit()
finally:
  connection.close()

"""

# create subroutine  
def insert_songs():
  try:
    # SongID field is auto increment (no data input required)
    #ask for user input for Title, Artist, Genre
    songTitle = input("Enter song Title: ")
    songArtist = input("Enter song Artist: ")
    songGenre = input("Enter song Genre: ")
    
    insert_query = "INSERT INTO songs(Title, Artist, Genre) VALUES(%s, %s, %s)"
    data_to_insert = (songTitle, songArtist, songGenre)
   # add data into the respective fields in the songs table
    dbCursor.execute(insert_query, data_to_insert)
    # save the changes permanently into the songs table in the database 
    connection.commit()
    

 
    # dbCursor.execute("INSERT INTO songs(Title, Artist, Genre) VALUES(?,?,?)", (songTitle, songArtist, songGenre))

    # connection.commit()

    print(f"{songTitle} Inserted in the songs table")
      
  except MySQLdb.Error as e:
      print(f"Error updating/adding record: {e}")

if __name__ == "__main__": # this make sure that if this file has been called, get executed and not any database's file has been called
    insert_songs()  # call/invoke the function
    
