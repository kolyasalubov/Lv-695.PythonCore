class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @staticmethod
    def counter():
        print(f"The total number of employees {Employee.count}")

    def employeeName(self):
        print(f"The name of employee is {self.name} and his/her salary is {self.salary}")


em1 = Employee('Sasha', 700)
em2 = Employee('Olya', 750)
em3 = Employee('Oleg', 800)

em1.employeeName()
em2.employeeName()
em3.employeeName()

Employee.counter()

print("Base:", Employee.__base__)
print("Dict:", Employee.__dict__)
print("Name:", Employee.__name__)
print("Module:", Employee.__module__)
print("Doc:", Employee.__doc__)
