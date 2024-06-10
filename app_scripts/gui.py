from tkinter import *

# Window initialization, name, and dimensions
window = Tk()
window.title("Shahyah's Recipe Scraper")
window.geometry('800x600')

# Config
window.config(bg='#30302f')

label = Label(window, text = "Hello World", font = ("Times New Roman", 50)
             , fg = "Light Grey", bg = "black", relief = "raised", bd = 10, padx=20, pady=20 )
label.place(x=100, y= 100)

window.mainloop()