# parent Class
class Car:

   
   total_car = 0 ## Class Varaibles 
   def __init__(self,brand, model):

       self.__brand = brand ## Createing the Private member in Class..
       self.model = model
       Car.total_car += 1
   def Full_name(self): # Print the full name of of Car with Brand and model..
        return f"{self.__brand} {self.model}"

   def get_brand(self): # Brand method to get the detail about brand.
        return self.__brand + "!" 


   
# Child class for inherit the Parent Class.
class Electric(Car):

    def __init__(self,brand,model,battery_size):
        # Super class that inherit the Car class with their member and member function.
        super().__init__(brand,model) # Sytax that use to access that inherit property.

        self.battery_size = battery_size




my_car = Car("Toyota","Supra") # Creating Object of Car..
print(my_car.get_brand) # get the brand name
New_car = Car("Buggati","Chiron Super Sprot 300")
print( New_car.model) # Access the Model name .
full = Car("fiat","gtr")
print(full.model)
print(full.Full_name())

elect = Electric("tata","BE6", "47Kwh")
print(elect.get_brand()) # get the brand method.

ele = Car.total_car
print(ele)



