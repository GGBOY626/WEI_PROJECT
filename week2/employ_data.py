class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Job Title: {self.job_title}")

    def give_raise(self, increase_money):
        self.salary += increase_money
        print(f"Updated salary for {self.name}: {self.salary}")
employee1 = Employee("Jack", 5000, "Manager")
employee2 = Employee("Rose", 4000, "Normal Staff")

# display info
employee1.display_info()
employee2.display_info()

# increase employee's salary
employee2.give_raise(500)

# display info to see updated salary
employee2.display_info()