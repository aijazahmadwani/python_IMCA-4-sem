class Person():
    def __init__ (self,person_name,age,address,height,weight): # constructor
        self.name=person_name
        self.age=age
        self.address=address
        self.height=height
        self.weight=weight
    def welcome(self):
        print("Welcome {}".format(self.name))
    def is_eligible(self):
        if(self.age>18):
            return True
        else:
            return False

person1=Person('aijaz',21,'ishber',2,67)
person1.welcome()
print(person1.is_eligible())
