class Employee:
    """This is docstring"""
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    def employee_info(self):
        print(f'The {self.name} has salary of {self.salary}$ a mouth')

    @staticmethod
    def total_employee_quantity():
        print(f'Total numbers of employees is {Employee.counter}')


if __name__ == "__main__":
    emp_1 = Employee('Oleh', 1000)
    emp_1.employee_info()
    emp_2 = Employee('Ilona', 1550)
    emp_2.employee_info()
    Employee.total_employee_quantity()
    emp_3 = Employee('Tanya', 2120)
    emp_3.employee_info()
    Employee.total_employee_quantity()
    Employee.__del__(emp_1)
    Employee.total_employee_quantity()

    print(Employee.__base__)
    print(Employee.__dict__)
    print(Employee.__name__)
    print(Employee.__module__)
    print(Employee.__doc__)
