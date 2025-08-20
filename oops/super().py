class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)   # calls Employee __init__
        self.department = department

    def display(self):
        print(f"Details:- \nName: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}")
        
mng = Manager("Sushil", 30000, "Testing")
mng.display()
