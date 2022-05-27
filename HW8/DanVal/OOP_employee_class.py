class Employee:

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
