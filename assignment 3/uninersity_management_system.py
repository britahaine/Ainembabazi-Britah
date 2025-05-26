class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id_number}")


class Student(Person):
    def __init__(self, name, id_number, age, program, cgpa):
        super().__init__(name, id_number)
        self.age = age
        self.program = program
        self.cgpa = cgpa

    def display_info(self):
        super().display_info()
        print(f"Age: {self.age}, Program: {self.program}, CGPA: {self.cgpa}")


class Lecturer(Person):
    def __init__(self, name, id_number, department, salary):
        super().__init__(name, id_number)
        self.department = department
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}, Salary: ${self.salary}")


class Staff(Person):
    def __init__(self, name, id_number, role, years_of_service):
        super().__init__(name, id_number)
        self.role = role
        self.years_of_service = years_of_service

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}, Years of Service: {self.years_of_service}")


student = Student("Ainembabazi Britah", "23007123", 21, "Software Engineering", 4.8)
lecturer = Lecturer("Dr. Joab Agaba", "LEC456", "Networks", 5000000)
staff = Staff("Bright Diaz", "STF789", "Administrator", 5)

# Display university information
print("=== University System ===")
print("Student Info:")
student.display_info()

print("\nLecturer Info:")
lecturer.display_info()

print("\nStaff Info:")
staff.display_info()
print("========================")
