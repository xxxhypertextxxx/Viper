# Imports

import databases_wip as db
import ultraColors as colors
from syntax import *
from tkinter.messagebox import showwarning

# Variables

fileExtension = ".vi"
dataBaseExtension = ".dbvi"

# Custom errors


class ViperRunError(Exception):
    pass

# Definitions


def run(code=None, file=None):
    if code is None:
        if file is None:
            raise ViperRunError("Error at <ViperFunction \"run()\">: \n \t No code or filepath was entered for the inter\
            peter")
        else:
            try:
                with open(file, "r") as runfile:
                    exec(str(runfile.read()))
                    if file[-2:] != "vi":
                        showwarning("Oh Noes", "Please make sure that the file's extension is \".vi\".")
            except FileNotFoundError:
                raise ViperRunError("Error at <ViperFunction \"run()\">: \n \t The filepath entered does not exsist or c\
                annot be found")
    else:
        exec(str(code))

# Main
