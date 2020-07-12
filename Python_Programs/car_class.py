class car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
    def get_description(self):
        d = self.name + " "+ self.model + " "+str(self.year)
        return d
my_car = car('BMW','a4',2003)
print(my_car.get_description())
