class Employee():
    def __init__(self, info_dict):
        self.info_dict = info_dict
        self.count_pip = len(info_dict)

    def employees(self):
        return f"The company has {self.count_pip} employees."

    def info(self):
        for k, v in (self.info_dict).items():
            print(f"{k} gets {v}$ per month.")

         
emp = Employee({"Andrey": 1500, "Oleg": 2000, "Anton": 2500})
emp.info()