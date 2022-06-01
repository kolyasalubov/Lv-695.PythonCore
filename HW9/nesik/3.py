class Employee():

    total_number_eployees = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.total_number_eployees += 1

    @classmethod
    def quantity_employees(cls) -> None:
        print(
            f'The total number of employees is: {Employee.total_number_eployees}')

    def salary_employee(self) -> None:
        print(f'The {self.name} salary is {self.salary}')

    def __del__(self) -> None:
        Employee.total_number_eployees -= 1


emp_1 = Employee('Oleh', 1400)
Employee.quantity_employees()
emp_2 = Employee('Mira', 500)
Employee.quantity_employees()
emp_3 = Employee('Hala', 700)
Employee.quantity_employees()


del emp_1
Employee.quantity_employees()


emp_2.salary_employee()
emp_3.salary_employee()

print(f'Information about the base classes: {Employee.__base__}')
print(f'The class namespace: {Employee.__dict__}')
print(f'The class name: {Employee.__name__}')
print(f'The module name: {Employee.__module__}')
print(f'The documentation bar: {Employee.__doc__}')
