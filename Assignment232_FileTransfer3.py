#       ============
#       Assignment 232
#       ============
#
#       Python:   3.8.5
#
#       Author:   Michael B. Darlow
#
#       Purpose:   The Tech Academy -- Python Course. File Transfer Assignment.
#                       Create a script that will automatically copy text files modified in the
#                       last 24 hours. 
#                       
#
#       Requirements:   -Allow user to choose a specific folder to be checked daily.
#                               -Allow user to choose a specific folder to receive copied files.
#                               -Allow user to manually initiate the file-check process.
#                               -
#                       
#
#
#

# Import modules:
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import shutil
import datetime
import glob


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Title:
        self.master.title("Check files")
        # If user clicks "X":
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master

        # Center app on the user's screen:
        center_window(self, 679, 225)
        
        # Browse source button:
        self.btn_browse_source = tk.Button(self.master,width=14,text="Browse...", font=("Helvetica", 13), command=lambda: browse_source(self) )
        self.btn_browse_source.grid(row=0,column=0,padx=(25,0),pady=(60,0) )
        # Browse destination button:
        self.btn_browse_dest = tk.Button(self.master,width=14,text="Browse...", font=("Helvetica", 13), command=lambda: browse_destination(self) )
        self.btn_browse_dest.grid(row=2,column=0,padx=(25,0),pady=(10,0) )
        # Check button:
        self.btn_check = tk.Button(self.master,width=14,height=2,text="Check for files...", font=("Helvetica", 13), command=lambda: check_files(self) )
        self.btn_check.grid(row=3,column=0,columnspan=1,padx=(25,0),pady=(10,0))
        # Close button:
        self.btn_check = tk.Button(self.master,width=14,height=2,text="Close Program", font=("Helvetica", 13), command=lambda: ask_quit(self) )
        self.btn_check.grid(row=3,column=2,padx=(365,0),pady=(10,0))

        # Browse source text box:
        self.txt_browse_source = tk.Entry(self.master,text=self.btn_browse_source, width=35, font=("Helvetica", 18) )
        self.txt_browse_source.grid(row=0, column=1, columnspan=2, padx=(40,0), pady=(60,0) )
        # Browse destination text box:
        self.txt_browse_dest = tk.Entry(self.master,text=self.btn_browse_dest, width=35, font=("Helvetica", 18) )
        self.txt_browse_dest.grid(row=2, column=1, columnspan=2, padx=(40,0), pady=(10,0) )


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Center GUI to user's screen:
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo

# Make sure user wants to exit program:
def ask_quit(self):
    if messagebox.askokcancel(title="Exit program", message="Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

# Browse for source folder:
def browse_source(self):
    
    # Make sure entry is blank:
    self.txt_browse_source.delete(0, END)
    
    root = Tk()
    root.withdraw()
    current_directory = filedialog.askdirectory()
    file_name = ""
    file_path = os.path.join(current_directory, file_name)
    self.txt_browse_source.insert(0, file_path)

# Browse for destination folder:
def browse_destination(self):

    # Make sure entry is blank:
    self.txt_browse_dest.delete(0, END)
    
    root = Tk()
    root.withdraw()
    current_directory = filedialog.askdirectory()
    file_name = ""
    file_path = os.path.join(current_directory, file_name)
    self.txt_browse_dest.insert(0, file_path)

def check_files(self):
    # Set source of files:
    source = self.txt_browse_source.get()
    # Set destination path:
    destination = self.txt_browse_dest.get()
    fileType = ".txt"
    # glob.glob() returns a list of file names within the source folder.
    # Return list of full file paths:
    files = glob.glob(source + "*" + fileType)
    for file in files:
        # Last Modified Time = file's modified time from timestamp in user's current time zone:
        LMTime = datetime.datetime.fromtimestamp(os.path.getmtime(file), tz=None)
        # Today's Date:
        TDate = datetime.datetime.today()

        # Create a list from the filepath:
        filePathList = file.split("\\")
        # The file name is the last element of the list:
        fileName = filePathList[-1]

        # Last Modified Time Limit = Last Modified Time + microsecond duration of one day:
        LMTimeLimit = LMTime + datetime.timedelta(days=1)

        # If modified in the last 24 hours:
        if LMTimeLimit > TDate:
            # copy2() preserves file metadata, such as modification times.
            # Copy to destination folder:
            shutil.copy2(file, destination + fileName)

    # If user selects both a source and destination folder:
    if source and destination:
        try:
            # If nothing is in selected folder:
            if not os.listdir(source):
                messagebox.showinfo(title="Source folder report", message="The selected source folder is empty.")
            # If there are files in selected folder, but none that are text files:
            elif not files:
                messagebox.showinfo(title="Source folder report", message="The selected source folder has no text (.txt) files for transfer.")
            # If there are text files in selected folder:
            else:
                # Let user know transfer is complete and ask whether user wants to continue:
                if not messagebox.askyesno(title="Transfer complete | Continue?", message="File transfer complete!\n\nDo you wish to continue?"):
                    self.master.destroy()
                    os._exit(0)
        # If folder doesn't exist:
        except (FileNotFoundError, NotADirectoryError):
            messagebox.showwarning(title="Folder not found!", message=f"One or more folder names were not found.\n\nAttempted source folder: {source}\nAttempted destination folder: {destination}")
    # If user doesn't select both folders:
    else:
        messagebox.showwarning(title="Select folders", message="Please select source and destination folders.")


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

