from tkinter import *

window=Tk()
window.title("Event Handler")
window.geometry("500x500")

input=Entry(window)
input.pack()

def handle_keypress(event):
    
    print(event.char)

window.bind("<Key>",handle_keypress)

def handle_click(event):
    print("\nHi")

button=Button(text="Click me!",relief=RAISED)
button.pack()

button.bind("<Button-1>",handle_click)

window.mainloop()