from tkinter import *
root = Tk()

def func():
    print("File opened")
mainMenu = Menu(root)

root.configure(menu=mainMenu)

subMenu = Menu(mainMenu)

mainMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label = "New File", command=func)
subMenu.add_separator()
subMenu.add_command(label = "open File", command=func) 
mainMenu.add_cascade(label = "Edit", menu=subMenu)

root.mainloop()