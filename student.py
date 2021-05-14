import course
from login import User
import pandas as pd
from course import Course

"""
df3 = a table with 3 column : title, major, name_pro
"""

df = pd.read_csv("course1.csv")
df3 = df[["title", "major", "name_pro"]]
df3_lst = df3.values.tolist()


class Student(User):
    def __init__(self, student_name, student_lastname, student_number, major, major_code, username, password,role,
                 status=True):
        self.student_name = student_name
        self.student_lastname = student_lastname
        self.student_number = student_number
        self.status = status
        self.total_units = 0
        self.taken_course = []

        super().__init__(student_name, student_lastname, student_number, username, password, major, major_code,role)

    def display_course(self):
        df4 = df[df3["major"] == self.major]
        return df4
    """
    df4 is a table with one column : major
    """
    def choose_course(self, course_name):
        df4 = df[df3["major"] == self.major]
        for lines in df4["title"]:
            if course_name in lines:
                self.total_units += course.unit
                course.capacity -= 1
                self.taken_course.append(course_name)
        return self.taken_course

    def rmv(self, course_name):
        for i in self.taken_course:
            if course_name == course.course_name:
                self.total_units -= course.unit
                course.capacity += 1
                self.taken_course.remove(course_name)
        return self.taken_course

    def __add__(self, other):
        total_units = self.total_units + other
        return total_units

    def __sub__(self, other):
        total_units = self.total_units - other
        return total_units

    def limitation_course(self):
        if 10 > self.total_units > 20:
            return False

    def display_taken_course(self):
        return self.taken_course

    def __str__(self):
        return f"name:{self.student_name}\n" \
               f"lastname :{self.student_lastname}\n" \
               f"student_number:{self.student_number}\n" \
               f"major :{self.major}\n" \
               f"major_code :{self.major_code} \n" \
               f"total units: {self.total_units}"
