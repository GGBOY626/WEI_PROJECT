# Base class Person
# This class stores the common attributes that all people in the university have.
# It demonstrates code reuse: name, address, age, and ID are shared by everyone.
class Person:
    def __init__(self, name, address, age, ID):
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID
# Student class (inherits from Person)
# Students have the same basic information as Person, but also have an academic record.
class Student(Person):
    def __init__(self, name, address, age, ID, academic_record):
        super().__init__(name, address, age, ID)
        self.academic_record = academic_record

# Staff class (inherits from Person)
# Staff members also need a tax code, which is specific to employees.
class Staff(Person):
    def __init__(self, name, address, age, ID, tax_code):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code

# Academic class (inherits from Staff)
# Academics are staff members, but they also have a salary attribute.
class Academic(Staff):
    def __init__(self, name, address, age, ID, tax_code, salary):
        super().__init__(name, address, age, ID, tax_code)
        self.salary = salary

# GeneralStaff class (inherits from Staff)
# General staff also inherit staff attributes but use pay_rate instead of salary.
class GeneralStaff(Staff):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID, tax_code)
        self.pay_rate = pay_rate

if __name__ == '__main__':
    s = Student("Alice", "123 St", 20, "S001", "A+")
    a = Academic("Bob", "456 St", 40, "A001", "T111", 80000)
    g = GeneralStaff("Charlie", "789 St", 35, "G001", "T666", 30.5)

    print(s.name, s.academic_record)  # Alice A+
    print(a.name, a.salary)  # Bob 80000
    print(g.name, g.pay_rate)  # Charlie 30.5
