# the steps was like:

# 1- connect.py (for connecting/creating tables)
# 2- createTbls.py(for creating tables within the dfe2.db)
# 3- addsongs.py (for inserting songs in the songs table)
# 4- readsongs.py(for reading songs from the songs table)



import sqlite3 as sql # import teh sql module


dbCon = sql.connect('Python\Week10 Code Template\Pt9_10DB\dfe2.db') # use the sqlite(sql) module # just created the file 'dfe2.db' file on the left

# create a cursor object/variable and assign it to the CURSOR method to run
dbCursor = dbCon.cursor()