import tkinter as tk
from speech2text import *

root = tk.Tk()
button_rec = tk.Button(root, text='Start', command=recognize)
button_rec.pack()
root.mainloop() 