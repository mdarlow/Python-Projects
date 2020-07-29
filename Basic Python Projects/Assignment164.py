#       ============
#       Assignment 164
#       ============
#       
#       Write a script that creates a database and adds new data into that database.
#       Requirements:
#       -Must use Python 3 & the SQLite3 module
#       -Must have two fields: An auto-increment primary integer field, and a field with the "string" datatype.
#       -The script must read from the following list of file names and determine only the .txt files:
#               fileList = ("information.docx", "Hello.txt", "myImage.png", \
#                               "myMovie.mpg", "World.txt", "data.pdf", "myPhoto.jpg")
#       -Next, script must add those .txt files within your database.
#       -Finally, script must legibly print qualifying text files to the console.
#
#

import os
import sqlite3

# Connect to database == 
conn = sqlite3.connect("Assignment164.db")
with conn:
    # Create cursor variable using cursor() method == 
    cur = conn.cursor()
    # Create table with auto-increment primary key integer & "string" fields == 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_1( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_1 TEXT \
                    )")
    # Save changes to database == 
    conn.commit()
# Close connection to database == 
conn.close()        

# Return list of file names in "Assignment164" folder ==
filenames = os.listdir(path="C:\\python_projects\\Assignment164\\") 

print("Text files in Assignment164 directory:")
conn = sqlite3.connect("Assignment164.db")
with conn:
    cur = conn.cursor()
    # Iterate through "Assignment164" folder == 
    for filename in filenames:
        # If it is a .txt file == 
        if filename.endswith(".txt"):
            # Add .txt files to database == 
            cur.execute("INSERT INTO tbl_1(col_1) VALUES (?)", (filename,) )
            print("  " + filename) 
conn.close()

