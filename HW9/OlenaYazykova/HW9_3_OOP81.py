class Employee:
    """Characteristic of employees"""

    count_employee=0

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        Employee.count_employee+=1
    
    def info_name_salary(self):
        return f"The name of employee is {self.name}, the salary is {self.salary}."
    
    def info_count_employee(self):
        return f'The total number of employees is {self.count_employee}.'

employee_1=Employee('Jhon', 1000)
employee_2=Employee('Jenny', 2000)
employee_3=Employee('Jack', 1500)
print(employee_1.info_count_employee())
print(employee_1.info_name_salary())
print(employee_2.info_name_salary())
print(employee_3.info_name_salary())
print('-----------------------------')
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
