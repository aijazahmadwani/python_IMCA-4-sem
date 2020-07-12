class Car:  # base / parent class
    def __init__ (self,model,year,topspeed):
        self.model=model
        self.year=year
        self.topspeed=topspeed
    def gearchange(self):
        print("gear changed")
    def info(self): # method overriding because derived class also has info method/func.
        print("car model is {} and car topspeed = {} ".format(self.model,self.topspeed))
class SportsCar(Car): # derived/child class
    def __init__(self,model,year,topspeed,acceleration,color):
        Car.__init__(self,model,year,topspeed)
        self.acceleration=acceleration
        self.color=color
    def info(self): # method overriding
        print("info of sports car")

class supersportscar(SportsCar):
    def __init__(self,model,year,topspeed,acceleration,color,horsepower):
        SportsCar.__init__(self,model,year,topspeed,acceleration,color)
        self.horsepower=horsepower
        
p=supersportscar("maruti",2017,300,"100kmp","black",5000)
p.info()
