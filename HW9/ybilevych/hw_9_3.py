class Employee:
    count = 0
    def __init__(self, name, sallary):
        Employee.count += 1
        self.name = name
        self.sallary = sallary

    def totalNumber(self):
        print(f"Total number of employees: {Employee.count}")

    def infoEmployee(self):
        print(f"Employee name {self.name}, sallary {self.sallary}.")


x1 = Employee('Jack', 10000)
x2 = Employee('June', 11000)

Employee.totalNumber(Employee)

x1.infoEmployee()

x2.infoEmployee()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)     
