from connect import *

# (1, 'Dance', 'AMJ', 'Coding')
# (2, 'Bad', 'MJ', 'Pop')

# create  subroutine
def update_songs():
  #use the primary key to update a single record

  idField = input("Enter the SongID of the record to be updated: ")

  #ask user the field to update
  fieldName = input("Enter Title or Artist or Genre as field name: ").title()

  # ask the user to provide the value/data for the field they want to update 
  fieldValue = input(f"Enter the value for {fieldName} field: ")

  print(fieldValue)

  # add single quotes around the field value because the data in the database has quotation around it already. 
  fieldValue = "'"+fieldValue+"'"
  print(fieldValue)


  #update a specific record
  'UPDATE songs SET Title or Artist or Genre  = {fieldValue} WHERE SongID =1/2/34.....'
  dbCursor.execute(f"UPDATE songs SET {fieldName} = {fieldValue} WHERE SongID = {idField}")
  dbCon.commit()

  print(f"Record {idField} updated in the songs table")
    
if __name__ == "__main__":
    update_songs()