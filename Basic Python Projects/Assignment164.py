#       ============
#       Assignment 164
#       ============
#
#       Python:   3.8.5
#
#       Author:   Michael Bradley Darlow
#
#       Purpose:   The Tech Academy -- Python Course. Write a program that 
#                       creates a database, determines which files within a folder are
#                       .txt files, and adds those .txt files into the database. 
#
#       Requirements:   -Must use Python 3 & the SQLite3 module.
#                               -Must have two fields: An auto-increment primary integer field, and a field with the "string" datatype.
#                               -The script must read from a list of file names and determine only the .txt files.
#                               -The script must add those .txt files within the database.
#                               -The script must legibly print qualifying text files to the console.
#
#

import os
import sqlite3

###########################
##   CREATE DATABASE     ##
###########################
# Connect to database:
conn = sqlite3.connect("Assignment164.db")
with conn:
    # Create cursor variable using cursor() method:
    cur = conn.cursor()
    # Create table with auto-increment primary key integer & "string" fields:
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_1( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_1 TEXT \
                    )")
    # Save changes to database: 
    conn.commit()
# Close connection to database:
conn.close()        

# Return list of file names in "Assignment164" folder:
filenames = os.listdir(path="C:\\python_projects\\Assignment164\\") 

############################
##       INSERT & DISPLAY     ##
############################
print("Text files in Assignment164 directory:")
conn = sqlite3.connect("Assignment164.db")
with conn:
    cur = conn.cursor()
    # Iterate through "Assignment164" folder:
    for filename in filenames:
        # If it is a .txt file:
        if filename.endswith(".txt"):
            # Add .txt files to database:
            cur.execute("INSERT INTO tbl_1(col_1) VALUES (?)", (filename,) )
            print("  " + filename) 
conn.close()

