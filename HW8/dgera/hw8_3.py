class Employee():
    """Employee Class"""

    employee_counter = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.employee_counter += 1
    
    @classmethod
    def quantityEmployees(cls) -> None:
        print(f'The total number of employees: {Employee.employee_counter}')
    
    def dataEmployee(self) -> None:
        print(f'{self.name}\'s salary is {self.salary}')
    
    def __del__(self) -> None:
        Employee.employee_counter -= 1


Emp_1 = Employee('Serhii', 1000)
Employee.quantityEmployees()
Emp_2 = Employee('Olha', 3000)
Employee.quantityEmployees()
Emp_3 = Employee('Mykola', 2000)
Employee.quantityEmployees()
del Emp_3
Employee.quantityEmployees()

print('===== Employee Data =====')
Emp_1.dataEmployee()
Emp_2.dataEmployee()

print('===== Additional information =====')
print(f'1. Information about the base classes: {Employee.__base__}')
print(f'2. The class namespace: {Employee.__dict__}')
print(f'3. The class name: {Employee.__name__}')
print(f'4. The module name: {Employee.__module__}')
print(f'5. The documentation bar: {Employee.__doc__}')