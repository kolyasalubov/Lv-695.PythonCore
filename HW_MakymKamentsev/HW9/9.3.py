class Employees:
    counter = 0
    def __init__(self, name,surname,salary,position):
        Employees.counter +=1
        self.name = name
        self.salary = salary
        self.surname = surname
        self.position = position

    def employees_counter(self):
        return Employees.counter

    def info(self):
        return f'name: {self.name}  surname: {self.surname} salary: {self.salary} postion: {self.position}'
employee_1 = Employees("Maks","Kamentsev",5000 ,"trainee")
employee_2 = Employees("Oleg","Ivanenko",15000, "big boss")

print(employee_1.info())
print(employee_2.info())
print(employee_2.employees_counter())


