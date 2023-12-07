

import readRemoteMySql, addSongsRemote, updateSongsRemote, deleteRemoteDB, reportsRemote

# function to read the respective menu files 
def menu_file():
  with open('RemoteDBserverSongsDB\songsMenuRemote.txt') as songsFile: # songsFile is a variable that is created just by this line and "with"
    userMenu = songsFile.read()
  return userMenu


# create the songsMenu
def songs_menu():
  option = 0 # initialise the option with an integer data type
  optionsList = ["1","2","3","4","5","6"] # list data structure with string data type
  # initialise the menu_file function with choiceMenu variable
  choiceMenu = menu_file()

  #create a while
  while option not in optionsList:
    # call/invoke the menu_file function through the choiceMenu variable
    print(choiceMenu)#  display the options from the menu file

    #re-assign the option variable with the input function
    option = input("Enter the option's number from below (the songs main menu): ") 

    # check if the use input from the option variable is a match with any of the options in the optionsList
    if option not in optionsList:
      # do this/execute the code below
      print(f"{option} is not a valid choice! ")# 0/7/8/9
  return option
# print(songs_menu())

# create a boolean variable 
mainProgram = True

while mainProgram: # while True
  #initialise the songs_menu function with mainMenu variable
  mainMenu = songs_menu()

  # if the user input is a string value 1
  if mainMenu == "1":
    # then go into readsongs file and call the read_songs() function 
    readRemoteMySql.read_songs()
  
  elif mainMenu == "2":
    addSongsRemote.insert_songs()

  elif mainMenu == "3":
    updateSongsRemote.update_songs()
  
  elif mainMenu == "4":
    deleteRemoteDB.delete_songs()
  
  elif mainMenu == "5":
    reportsRemote.songs_reports()

  else: # this exits the program
    # re-assign the boolean variable of 'mainProgram' to False
    mainProgram = False
input("Enter to quit the songs App")


