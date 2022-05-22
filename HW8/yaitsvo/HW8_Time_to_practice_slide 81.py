class Employee:
    """Class with Employees"""
    employes_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.employes_count += 1

    def get_info(self):
        print(f'Employee name: {self.name}, salary: {self.salary}')

    def get_count(self):
        print(f'Total number of employees: {Employee.employes_count}')

e1 = Employee('Ivan', 2000)
e2 = Employee('Lesya', 3000)
e1.get_info()
Employee.get_count(Employee)

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
