class Mobile:
    def __init__ (self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price


nokia=Mobile("nokia","nokia 3311",3000)
iphone=Mobile("Apple","iphone 5",50000)
print("Model name of nokia is {}".format(nokia.model_name))
