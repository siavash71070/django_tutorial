
class Employee:
    salary = 3000

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def salary_view(self):
        print(f"The employee's salary is: ${self.salary}")


# initiate the class
employee1 = Employee("John", "Doe")
print(employee1.full_name())
employee1.salary_view()
