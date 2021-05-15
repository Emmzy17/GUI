from tkinter import *
root = Tk()

label1 = Label(root, text="Enter you expression")
label1.pack()

def evaluate(event):
    data=e.get()
    ans.configure(text='Answer:' + str(eval(data)))

e = Entry(root)
e.bind('<Return>', evaluate)
e.pack()

ans = Label(root)
ans.pack()

root.geometry('300x200')
root.title('Calculator')

root.mainloop()