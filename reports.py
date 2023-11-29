# The fake data in songs.sql for test was generated from https://www.mockaroo.com/

from connect import *

# create subroutine 
def songs_reports():

  # dbCursor.execute("SELECT * FROM songs ORDER BY songID DESC")
  # dbCursor.execute("select Artist, Tite FROM songs")
  # dbCursor.execute("SELECT * FROM songs where Genre = 'pop' ")
  # dbCursor.execute("")
  dbCursor.execute("SELECT * FROM songs WHERE artist LIKE '%a%' ")
  # dbCursor.execute("")
  # dbCursor.execute("")
  # dbCursor.execute("")


  reports = dbCursor.fetchall()

  for aRecord in reports:
      print(aRecord)

if __name__ == "__main__":
  songs_reports()