
class Car:
   def __init__(self,brand, model):

       self.__brand = brand
       self.model = model
   def Full_name(self):
        return f"{self.__brand} {self.model}"

   def get_brand(self):
        return self.__brand + "!"


class Electric(Car):

    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = Car("Toyota","Supra")
print(my_car.get_brand)
New_car = Car("Buggati","Chiron Super Sprot 300")
print( New_car.model)
full = Car("fiat","gtr")
print(full.model)
print(full.Full_name())

elect = Electric("tata","BE6", "47Kwh")
print(elect.get_brand())



