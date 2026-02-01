from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("500x800")

def msg():
    messagebox.showwarning("Alert!","Stop! Virus Found")


button=Button(root,text="Scan for Virus",command=msg)
button.place(x=200,y=80)

def info():
    messagebox.showinfo("Information","My name is Sai.")

button=Button(root,text="Click for Info",command=info)
button.place(x=200,y=160)


def err():
    messagebox.showerror("Error!","Not recognised device!")
button=Button(root,text="Error Message",command=err)
button.place(x=200,y=240)

def askq():
    messagebox.askquestion("Question!","Do you like Coding?")

button=Button(root,text="Click for question",command=askq)
button.place(x=200,y=320)

def askok():
    messagebox.askokcancel("Permission","Can this app download these files?")
button=Button(root,text="Download Files",command=askok)
button.place(x=200,y=400)

def askyn():
    messagebox.askyesno("Question","Cricket is better than football")
button=Button(root,text="Yes or No?",command=askyn)
button.place(x=200,y=480)

def askretryandcancel():
    messagebox.askretrycancel("System Failure","Do you want the system to try again?")
button=Button(root,text="Retry or Cancel",command=askretryandcancel)
button.place(x=200,y=560)


root.mainloop()