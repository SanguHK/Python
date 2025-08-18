from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turnon(self):
        pass

    @abstractmethod
    def turnoff(self):
        pass


class Fan(Appliance):
    def __init__(self, name):
        self.name = name

    def turnon(self):
        print(f"The {self.name} turned on")

    def turnoff(self):
        print(f"The {self.name} turned off")


class Light(Appliance):
    def __init__(self, name):
        self.name = name

    def turnon(self):
        print(f"The {self.name} turned on")

    def turnoff(self):
        print(f"The {self.name} turned off")


# Create objects
applns = [Fan("Bajaj"), Light("Havells")]

for i in applns:
    i.turnon()
    i.turnoff()
