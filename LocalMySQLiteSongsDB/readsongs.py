from connect import *

# create subroutine 
def read_songs():

    # select all records from songs
    dbCursor.execute("SELECT * FROM songs")
    #fetch/get all songs from the songs table
    allRecords = dbCursor.fetchall()

# 'method2'
# allRecords = dbCursor.execute('select * from dongs').fetchall()

    # loop through and display all records from the songs table
    for eachRecord in allRecords:
        print(eachRecord)

if __name__ == "__main__": # this make sure that if this file has been called, get executed and not any database's file has been called
    read_songs()