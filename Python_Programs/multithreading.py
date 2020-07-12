from threading import Thread
import time
class threading(Thread):
    
    def __init__(self,initial,end,delay):
        super().__init__()
        self.initial=initial
        self.end=end
        self.delay=delay
    def run(self):
        for i in range(self.initial,self.end):
            print(str(i)+"\t")
            time.sleep(self.delay)
        
t1=threading(1,11,1)
t1.start()
t2=threading(11,21,2)
t2.start()
t3=threading(21,31,3)
t3.start()
