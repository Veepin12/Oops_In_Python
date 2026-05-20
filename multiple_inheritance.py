class Engine:
    def __init__(self, engine_name):
        self.engine_name = engine_name

    def print_type(self):
        return self.engine_name


class Body:
    def __init__(self, body_type):
        self.body_type = body_type

    def get_body_type(self):
        return self.body_type


class BHP:
    def __init__(self, horse_power, torque):
        self.horse_power = horse_power
        self.torque = torque

    def spec(self):
        return f"{self.horse_power} hp, {self.torque} Nm"


class CarName(Engine, Body, BHP):
    def __init__(self, engine_name, body_type, horse_power, torque, name):
        Engine.__init__(self, engine_name)
        Body.__init__(self, body_type)
        BHP.__init__(self, horse_power, torque)
        self.name = name

    def model(self):
        return self.name


car = CarName("V8 Twin Turbo", "Sedan", 635, 750,"BMW M5 CS")

print(car.print_type())
print(car.get_body_type())
print(car.spec())
print(car.model())