class Employee:
    """Employee class"""
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @staticmethod
    def get_counter():
        return f"Number of employees - {Employee.counter}"

    def employee_character(self):
        return f"Employee name: {self.name}, salary: {self.salary}"


first_employee = Employee("Max", 1000)
print(first_employee.employee_character())
second_employee = Employee("Vlad", 2000)
print(second_employee.employee_character())
third_employee = Employee("Oleg", 3000)
print(third_employee.employee_character())
print(Employee.get_counter())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
        
        