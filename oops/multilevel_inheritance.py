class Vehicle:
    def __init__(self,max_speed):
        self.max_speed = max_speed
class Car(Vehicle):
    def __init__(self,max_speed,fuel_type):
        super().__init__(max_speed)
        self.fuel_type = fuel_type
        
class ElectricCar(Car):
    def __init__(self,max_speed,fuel_type,battery_capacity):
        super().__init__(max_speed,fuel_type)
        self.battery_capacity = battery_capacity
    def car_info(self):
        print(f"Car details: \n max_speed : {super().max_speed} \n fuel_type : {super().fuel_type} \n Battery capacity : {battery_capacity}hr")
        
mycar = ElectricCar(120,"petrol",10)
mycar.car_info()

class Vehicle:
    def __init__(self,max_speed):
        self.max_speed = max_speed
class Car(Vehicle):
    def __init__(self,max_speed,fuel_type):
        super().__init__(max_speed)
        self.fuel_type = fuel_type
        
class ElectricCar(Car):
    def __init__(self,max_speed,fuel_type,battery_capacity):
        super().__init__(max_speed,fuel_type)
        self.battery_capacity = battery_capacity
    def car_info(self):
        print(f"Car details: \n max_speed : {super().max_speed} \n fuel_type : {super().fuel_type} \n Battery capacity : {battery_capacity}hr")
        
mycar = ElectricCar(120,"petrol",10)
mycar.car_info()

class Vehicle:
    def __init__(self,max_speed):
        self.max_speed = max_speed
class Car(Vehicle):
    def __init__(self,max_speed,fuel_type):
        super().__init__(max_speed)
        self.fuel_type = fuel_type
        
class ElectricCar(Car):
    def __init__(self,max_speed,fuel_type,battery_capacity):
        super().__init__(max_speed,fuel_type)
        self.battery_capacity = battery_capacity
    def car_info(self):
        print(f"Car details:-\n max_speed : {self.max_speed} km\h\n fuel_type : {self.fuel_type} \n Battery capacity : {self.battery_capacity}hr")
        
mycar = ElectricCar(120,"petrol",10)
mycar.car_info()