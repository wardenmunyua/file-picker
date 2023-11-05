from tkinter import Tk
from tkinter.filedialog import askopenfilename

#Tk.withdraw() can be used to prevent the main window from opening
filename = askopenfilename()
print(filename)
