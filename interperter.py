# Imports

import ultraColors as colors # A module with tons of colors
import databases_wip as db # A module for databases(WIP)
from syntax import *
from tkinter.messagebox import showwarning

# Variables

fileExtension = ".vi"
dataBaseExtension = ".dbvi"

# Custom errors

class ViperRunError(Exception):
    pass

# Definitions

def run(code=None,file=None):
    if code == None:
        if file == None:
            raise ViperRunError("Error at <ViperFunction \"run()\">: \n \t No code or filepath was entered for the interperter")
        else:
            try:
                with open(file, "r") as runfile:
                    exec(str(runfile.read()))
                    if file[-2:] != "vi":
                        showwarning("Oh Noes", "Please make sure that the file's extension is \".vi\".")
            except FileNotFoundError:
                raise ViperRunError("Error at <ViperFunction \"run()\">: \n \t The filepath entered does not exsist or cannot be found")
    else:
        exec(str(code))

# Main
