# 54. Class Method


class Student:

    count = 0
    total_grade = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        Student.count += 1
        Student.total_grade += grade

    def get_info(self):
        return f"{self.name} = {self.grade}"

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_average_grade(cls):
        if cls.count == 0:
            return 0

        return cls.total_grade / cls.count


count = Student.get_count()
average_grade = Student.get_average_grade()
print(f"Student count: {count}, Average grade: {average_grade}")

student1 = Student("Alice", 3.2)
student2 = Student("Bob", 2.8)
student3 = Student("Charlie", 4.0)

count = Student.get_count()
average_grade = Student.get_average_grade()
print(f"Student count: {count}, Average grade: {average_grade:.2f}")
