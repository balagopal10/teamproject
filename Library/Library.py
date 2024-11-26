from employee import Employee

class Librarys:
    def __init__(self):
        self.employees = []

    def create_employee(self, employee):
        self.employees.append(employee)
        return f"Employee {employee.name} added successfully!"

    def read_employees(self):
        return self.employees if self.employees else "No employees found."

    def update_employee(self, name, **kwargs):
        for emp in self.employees:
            if emp.name == name:
                for key, value in kwargs.items():
                    if hasattr(emp, key):
                        setattr(emp, key, value)
                return f"Employee {name} updated successfully!"
        return f"Employee {name} not found."

    def delete_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                return f"Employee {name} deleted successfully!"
        return f"Employee {name} not found."
