import random

class Employee:
    def __init__(self, FirstName, LastName) -> None:
        self.FirstName = FirstName
        self.LastName = LastName
        self.Fullname = self.FirstName + " " + self.LastName
        self.Email = self.FirstName.lower() + "." + self.LastName.lower().rstrip() + "@company.com"
        self.EmployeeID = 0

    def get_email_address(self, id):
        self.EmployeeID = id
        return self.Email

    def print_details(self):
        print('Name:', self.Fullname)
        print('Email:', self.Email)
        print('Employee ID:',self.EmployeeID)

with open('employees.txt', 'r') as file:
    employees_data = file.readlines()
    employees = []

    for employee_data in employees_data:
        names = employee_data.split(' ')
        first_n = names[0]
        last_n = names[1]
        employee = Employee(first_n, last_n)
        employees.append(employee)
    
    for employee in employees:
        print(employee.print_details())