from tkinter import *
parent = Tk()
redbutton = Button(parent,text = "red",fg = "red")
redbutton.pack(side = LEFT)

greenbutton = Button(parent,text = "green",fg = "green")
greenbutton.pack(side = RIGHT)

bluebutton = Button(parent,text = "blue",fg = "blue")
bluebutton.pack(side = TOP)

blackbutton = Button(parent,text = "black",fg = "black")
blackbutton.pack(side = BOTTOM)

parent.mainloop()
