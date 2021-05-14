import csv
import pandas as pd
from login import User

from student import Student

file_path = "course1.csv"
df_course = pd.read_csv(file_path)
course_lst = df_course.values.tolist()

file_path1 = "student1.csv"
df_course = pd.read_csv(file_path1)
student_lst = df_course.values.tolist()


class admin(User):
    def define_course(self, course_name, professor, course_number, capacity):
        input_lst = [course_name, professor, course_number, capacity]
        course_lst.append(input_lst)
        return course_lst

    def see_lst_students(self, student_lst):
        for student in student_lst:
            if student.major_code == self.major_code:
                student_lst.add([student.student_name, student.student_lastname,
                                 student.student_number, student.major, student.major_code,
                                 student.username, student.password])
        return student_lst

    def select_student(self, student_number):
        if student_number == student.student_number:
            return True
