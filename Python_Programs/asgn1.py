from threading import Thread
import time
import os
class Printer(Thread):
    def run(self):
        for i in range(100):
            print(i)
            time.sleep(1)
    
class FileHandler:
    def __init__(self,name):
         self.name = name
         self.file =  open(self.name,"w")
         self.file.close()
    def read(self):
        try:
            self.file = open("test12345.txt","r")
        except:
            open("test12345.txt","w")
            self.read()
        print(self.file.read())
        self.file.close()
        input("")

    def write(self,text):
        self.file = open("test1234.txt","a")
        self.file.write(text+"\n")
        self.file.close()


printer = Printer()
printer.start()

handler = FileHandler()
exitFlag = False

while(not exitFlag):
    os.system("clear")
    print('''
        ---- MENU ----
          1. READ
          2. WRITE
          3. EXIT
        '''
        )
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        choice = -1
    if choice == 1:
            handler.read()
    elif choice == 2:
        handler.write(input("Enter Text to Write: "))
    elif choice == 3:
            exitFlag = True
    else:
        print("Incorrect Choice, do again")
        input("")

              
