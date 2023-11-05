from tkinter import Tk                                      #for version <3 use 'Tkinter' instead of 'tkinter'
from tkinter.filedialog import askopenfilename

#Tk.withdraw() can be used to prevent the main window from opening
filename = askopenfilename()
print(filename)
