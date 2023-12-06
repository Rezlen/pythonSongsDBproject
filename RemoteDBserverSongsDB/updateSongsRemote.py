from mainRemoteDB import *

# (1, 'Dance', 'AMJ', 'Coding')
# (2, 'Bad', 'MJ', 'Pop')

# create  subroutine
def update_songs():
  #use the primary key to update a single record
  try:
    idField = input("Enter the SongID of the record to be updated: ")
    #ask user the field to update
    fieldName = input("Enter one of following three: 'Title' or 'Artist' or 'Genre' that you want to change: ").title()
    # ask the user to provide the value/data for the field they want to update 
    fieldValue = input(f"Enter the value for {fieldName} that you want to change with: ")
    print(f" You are replaced '{fieldValue}' in '{fieldName}' column for record '{idField}' .")
    
    update_query = f"UPDATE songs SET {fieldName} = %s WHERE SongID = %s"
    data_to_insert = (fieldValue, idField)
    # Execute the update query with parameters
    dbCursor.execute(update_query, data_to_insert)
    connection.commit()
    
    # 'UPDATE songs SET Title or Artist or Genre  = {fieldValue} WHERE SongID =1/2/34.....'
    # dbCursor.execute(f"UPDATE songs SET {fieldName} = {fieldValue} WHERE SongID = {idField}")

    # # add single quotes around the field value because the data in the database has quotation around it already. 
    # fieldValue = "'"+fieldValue+"'"
    # print(fieldValue)
    # connection.commit()

    print(f"Record {idField} updated in the songs table")
  except MySQLdb.Error as e:
    print(f"Error updating record: {e}")
    
if __name__ == "__main__":
  update_songs()