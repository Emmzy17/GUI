import tkinter.messagebox

tkinter.messagebox.showinfo("Window Title", "Do you know the world just blew up")

ans = tkinter.messagebox.askquestion("Verification", "Are you human")

if ans == 'yes':
    tkinter.messagebox.showinfo("Congratulations", "You are human; verification passed")
if ans == 'no':
    tkinter.messagebox.showinfo("Wow", "You are a bot; Verification Failed")