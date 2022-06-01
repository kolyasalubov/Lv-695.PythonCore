class Employee:
    """Employee characteristic"""
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @staticmethod
    def get_counter():
        return f"Number of employees {Employee.counter}"

    def employee_info(self):
        return f"Employee name: {self.name}, salary: {self.salary}"


first_employee = Employee("Viktor", 1000)
print(first_employee.employee_info())
second_employee = Employee("Oleg", 8000)
print(second_employee.employee_info())
third_employee = Employee("Nazar", 3000)
print(third_employee.employee_info())
print(Employee.get_counter())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)