class Employee:
    def  __init__(self,employeeName,age):
        self.employeeName= employeeName
        self.age=age

    def display(self):
        print(f"The employee name is {self.employeeName} and age is {self.age}") 