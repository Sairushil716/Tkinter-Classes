from tkinter import *

root=Tk()
root.title("Number Pad")
#Size of the screen
root.geometry("250x300")

#Create a frame to organise better
#frame=Frame(master=root, height=200, width=360, bg="#d0efff")

nums=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]

for i in range(4):
    root.columnconfigure(i,weight=1,minsize=150)
    root.rowconfigure(i,weight=1,minsize=100)
    for j in range(0,3):
        frame=Frame(master=root,relief=RAISED,
        borderwidth=1)

        frame.grid(row=i,column=j)
        label=Label(master=frame,text=nums[i][j], bg="#d0eFFF")
        label.pack(padx=3,pady=3)

root.mainloop()