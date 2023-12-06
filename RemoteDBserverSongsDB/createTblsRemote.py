from mainRemoteDB import * # import the connect.py module 

try:
  
  # # Create 'members' table
  # dbCursor.execute("""
  # CREATE TABLE members (
  #     MemberID INT NOT NULL AUTO_INCREMENT,
  #     Firstname TEXT,
  #     Lastname TEXT,
  #     Email TEXT,
  #     PRIMARY KEY(MemberID)
  # )""")

  # # Create 'songs' table
  # dbCursor.execute("""
  # CREATE TABLE songs (
  #     SongID INT NOT NULL AUTO_INCREMENT,
  #     Title TEXT,
  #     Artist TEXT,
  #     Genre TEXT,
  #     PRIMARY KEY(SongID)
  # )""")

  # Create 'downloads' table with foreign keys
  dbCursor.execute("""
  CREATE TABLE downloads (
    DownlID INT NOT NULL AUTO_INCREMENT,
    Date TEXT,
    PRIMARY KEY(DownlID),
    songs_SongID INT,
    members_MemberID INT,
    KEY songs_SongID_id_idx (songs_SongID),
    KEY members_MemberID_id_idx (members_MemberID)
         
  )""")
  
  # droping a table
  # dbCursor.execute("DROP TABLE downloads")
  # dbCursor.execute("ALTER TABLE downloads ADD FOREIGN KEY (SongID) REFERENCES songs(SongID)")
      
  # KEY parent_id_idx (parent_id),
  # UNIQUE INDEX 'SongID_id_idx' ('songs_SSongID'),
  # UNIQUE INDEX 'MemberID_id_idx' ('members_MemberID')
  
    # songs_SongID INT,
    # members_MemberID INT,
    # KEY songs_SongID_id_idx (songs_SongID),
    # KEY members_MemberID_id_idx (members_MemberID)
    
  # KEY songs_SongID_idx (songs_SongID),
  # KEY members_MemberID_idx (members_MemberID)
  
  # Using FK is not allowed in PlanetScale MySql website 
  # FOREIGN KEY(SongID) REFERENCES songs(SongID),
  # FOREIGN KEY(MemberID) REFERENCES members(MemberID)

  """
  https://planetscale.com/docs/learn/operating-without-foreign-key-constraints
  How does your schema look without FOREIGN KEY constraints?
  The above schema would look exactly the same, minus the CONSTRAINT clause:
  CREATE TABLE parent_table (
  id INT NOT NULL,
  PRIMARY KEY (id)
  );

  CREATE TABLE child_table (
  id INT NOT NULL,
  parent_id INT,
  PRIMARY KEY (id),
  KEY parent_id_idx (parent_id)
  );

  """

  print("Tables by createTblsRemote.py created successfully")

except MySQLdb.Error as e:
  print("Error creating tables:", e)

finally:
  connection.close()