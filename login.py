import pandas as pd
import hashlib
import csv


class User:
    def __init__(self, username, password, student_name, student_lastname, student_number, major, major_code,role):
        self.username = username
        self.password = password
        self.student_name = student_name
        self.student_lastname = student_lastname
        self.student_number = student_number
        self.major = major
        self.major_code = major_code
        self.role = role

    @staticmethod
    def register():
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account["username"])

        username = input("enter your username:")
        if username in lst_username:
            print("valid username")
        password = input("enter your password:")
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        obj_user = User(username, hash_password)

        row_account = [[obj_user.username, obj_user.password]]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            csv_writer.writerows(row_account)

    @staticmethod
    def login():
        file_path = "account1.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account["username"])
        lst_password = list(df_account["password"])
        while True:
            username = input("enter your username:")
            if username in lst_username:
                print(f" {username} valid ")
                n = 1
                while n < 3:
                    password = input(f"{username} enter your password :")
                    hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
                    if password in lst_password:
                        print(f"{username} entered successfully ")
                    else:
                        print("invalid")

            else:
                print(f"{username}invalid")
