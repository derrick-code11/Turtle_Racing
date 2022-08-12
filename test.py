import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

image = Image.open('road.gif')
tk_image = ImageTk.PhotoImage(image)

label = tk.Label(root, text='Some Plain Text', image=tk_image)
label.pack()

root.mainloop()