# 47. Class Variable


class Student:

    class_year = 2024
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Student.num_student += 1


student1 = Student("John", 20)
student2 = Student("Doe", 38)
student3 = Student("Bro", 12)
student4 = Student("Code", 4)

print(
    f"student 1 name '{student1.name}', {student1.age} years old. Graduated year {Student.class_year}"
)

print(
    f"student 2 name '{student2.name}', {student2.age} years old. Graduated year {Student.class_year}"
)


# Exercise

print(
    f"My graduating class of {Student.class_year} has {Student.num_student} students."
)
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
