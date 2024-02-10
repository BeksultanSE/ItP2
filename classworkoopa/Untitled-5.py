class Employee:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        self.fullname = f"{first} {last}"
        self.email = f"{first.lower()}.{last.lower()}@company.com"

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.fullname)  
print(emp_2.email)  
print(emp_3.firstname)  
