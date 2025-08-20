class Teacher:
    def teach(self):
        print("I am teaching")
        
class Singer:
    def sing(self):
        print("I am singing")
    
class Person(Teacher, Singer):
    def info(self):
        # Call methods directly
        self.teach()
        self.sing()

# Create object
vishu = Person()
vishu.info()
