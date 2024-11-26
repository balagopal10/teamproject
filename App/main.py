from Library import Library
from employee import Employee
from validation import validate_name, validate_age, validate_doj
import datetime

class App:
    def __init__(self):
        self.lib = Library()

    def menu(self):
        while True:
            print("\n------ Employee Management System -------")
            print("1. Create Employee")
            print("2. View All Employees")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_employee(self):
        try:
            name = input("Enter name : ")
            validate_name(name)
            age = int(input("Enter age : "))
            validate_age(age)
            doj = input("Enter Date of Joining (YYYY-MM-DD): ")
            validate_doj(doj)
            created_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            emp = Employee(name, age, doj, created_on)
            print(self.lib.create_employee(emp))
        except ValueError as e:
            print(f"Error: {e}")

    def view_employees(self):
        employees = self.lib.read_employees()
        if isinstance(employees, list):
            for emp in employees:
                print(emp)
        else:
            print(employees)

    def update_employee(self):
        name = input("Enter the name of the employee to update: ")
        updates = {}
        while True:
            field = input("Enter the field to update (name, age, doj, is_active) or 'done' to finish: ")
            if field == "done":
                break
            value = input(f"Enter the new value for {field}: ")
            if field == "age":
                value = int(value)
            elif field == "is_active":
                value = value.lower() == "true"
            updates[field] = value
        print(self.lib.update_employee(name, **updates))

    def delete_employee(self):
        name = input("Enter the name of the employee to delete: ")
        print(self.lib.delete_employee(name))

if __name__ == "__main__":
    app = App()
    app.menu()
