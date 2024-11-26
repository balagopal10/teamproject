class Employee:
    def  __init__(self,employeeName,age,doj,createdOn,isActive):
        self.employeeName= employeeName
        self.age=age
        self.doj=doj
        self.createdOn=createdOn
        self.isActive=isActive

    def display():
        print("The Employee details are :")
        print(f"Employee name : {self.employeeName}")
        print(f"Age : {self.age}")
        print(f"Date of Joining : {self.doj}")
        print(f"Activity Status : {self.isActive}")
    