# Michael Ressler
# Outlab5 
# Python
 
from tkinter import *
master = Tk()

canvas_width = 400
canvas_height = 400
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

w.create_rectangle(0, 0, 400, 400, fill="green")
y = int(canvas_height / 2)
w.create_oval(50,50,350,350)
w.create_oval(125,125,200,200)
w.create_oval(205,125,285,200)
w.create_line(150,275,250,275)

f = Frame(master, height=50, width=50)
f.pack_propagate(0) # don't shrink
f.pack()

def quit():
    w.destroy()
    exit()

b = Button(master, text="Quit", command=quit)
b.pack(fill=BOTH, expand=1)

#eyes
def clear():
    w.delete("all")
    w.create_rectangle(0, 0, 400, 400, fill="green")
    y = int(canvas_height / 2)
    w.create_oval(50,50,350,350)
    w.create_oval(105,105,185,185)
    w.create_oval(210,130,290,205)
    w.create_line(150,275,250,275)

b = Button(master, text="Eyes", command=clear)
b.pack(fill=BOTH, expand=1)

#talk
def clear1():
    w.delete("all")
    w.create_rectangle(0, 0, 400, 400, fill="green")
    y = int(canvas_height / 2)
    w.create_oval(50,50,350,350)
    w.create_oval(125,125,200,200)
    w.create_oval(205,125,285,200)
    w.create_line(150,275,250,275)
    w.create_line(150,275,160,290) #new 
    w.create_line(160,290,240,290) #new 
    w.create_line(250,275,240,290) #new 

b = Button(master, text="Talk", command=clear1)
b.pack(fill=BOTH, expand=1)


mainloop()

