class livingBeing:
    def display(self):
        print("Parent class")
        
class Animal(livingBeing):
    def display(self):
        super().display()
        print("Animal class")
        
class Plant(livingBeing):
    def display(self):
        super().display()
        print("Plant class")
        
class Human(livingBeing,Animal):
    def display(self):
        self.display()
        self.display()
        print("Human class")
        
obj = Human()
obj.display()
