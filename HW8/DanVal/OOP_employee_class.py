class Employee(object):

    employee_calc = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_calc += 1

    def total_employees():
        return Employee.employee_calc
    
    def information(self):
        return f"Employee name - {self.name}. He/She has salary - {self.salary}"
    
    def __del__(self):
        print(f"I'm deleting you data, Mr.{self.name}.\nWith love, your GarbageCollector.\nHA-HA-HA-HUM")

# function out of class
def all_information(my_class):
    return f"Parent's class is {(my_class.__base__)}.\nThe class namespace - {my_class.__dict__}\nClass name - {my_class.__name__}\nThe module name in which the class is defined {my_class.__module__}\nThe documentation bar - {my_class.__doc__}"

    
a = Employee('Ashot', 1000)

print(all_information(Employee))
# my_value = {'Parent class is': '__base__','The class namespace': '__dict__','Class name': '__name__','The module name in which the class is defined': '__module__','The documentation bar ': '__doc__'}
