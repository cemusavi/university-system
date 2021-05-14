import pandas as pd
import sys

df = pd.read_csv("course1.csv")
df1 = df[["major", "title"]]


class Course:

    def __init__(self, title, professor, course_id, unit, capacity, major, major_id, total_unit=None):
        self.title = title
        self.Professor_name = professor
        self.course_id = course_id
        self.unit = unit
        self.capacity = capacity
        self.remain_capacity = capacity
        self.total_unit = total_unit
        self.major_id = major_id
        self.major = major

    def __sub__(self, other):
        self.remain_capacity = self.remain_capacity - other
        yield self
        if self.remain_capacity > 0:
            yield True

    def check(self):
        if self.remain_capacity> 0:
            return True

    def __str__(self):
        return f"Title : {self.title} \n" \
               f"Professor : {self.Professor_name} \n" \
               f"ID Course : {self.course_id} \n" \
               f"Unit : {self.unit} \n" \
               f"Capacity : {self.capacity} \n" \
               f"Remain Capacity: {self.remain_capacity} \n" \
               f"Total Unit: {self.total_unit}" \
               f"ID Major: {self.major_id}"


