from tkinter import *
from functools import partial
from tkinter import messagebox
root =Tk()

root.geometry('800x400')
root.title('Library Management Software')
def fun():
   # root.destroy()
    top=Tk()
    #top.geometry("800x400")
    frame=Frame(top)
    frame.pack()
    bt=Button(frame,text="22").grid(row=3,column=2)
    top.mainloop()

addBook=Button(root,text="ADD BOOK",command=fun).grid(row=0,column=15)
deleteBook=Button(root,text="DELETE BOOK").grid(row=1,column=15)
searchBook=Button(root,text="SEARCH BOOK").grid(row=2,column=15)
updateBook=Button(root,text="UPDATE BOOK").grid(row=3,column=15)
viewBooks=Button(root,text="VIEW BOOKS").grid(row=4,column=15)
issueBook=Button(root,text="ISSUE BOOK").grid(row=5,column=15)
viewIssuedBooks=Button(root,text="VIEW ISSUED BOOKS").grid(row=6,column=15)
removeIssuedBook=Button(root,text="REMOVE ISSUED BOOK").grid(row=7,column=15)
root.quit()
root.mainloop()
