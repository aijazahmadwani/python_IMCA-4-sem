from tkinter import *
top=Tk()
def hello():
    print("hello world")

menubutton=Menubutton(top)
menubar.add_command(label="hello",command=hello)
menubar.add_command(label="quit",command=top.quit)

top.config(menu=menubar)
top.mainloop()