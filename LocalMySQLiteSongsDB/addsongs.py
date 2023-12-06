from connect import * 

# create subroutine  
def insert_songs():
    # SongID field is auto increment (no data input required)
    #ask for user input for Title, Artist, Genre
    songTitle = input("Enter song Title: ")
    songArtist = input("Enter song Artist: ")
    songGenre = input("Enter song Genre: ")

    # add data into the respective fields in the songs table
    dbCursor.execute("INSERT INTO songs(Title, Artist, Genre) VALUES(?,?,?)", (songTitle, songArtist, songGenre))
    # save the changes permanently into the songs table in the databse 
    dbCon.commit()

    print(f"{songTitle} Inserted in the songs table")

if __name__ == "__main__": # this make sure that if this file has been called, get executed and not any database's file has been called
    insert_songs()  # call/invoke the function