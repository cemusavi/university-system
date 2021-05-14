from login import User

print("please enter one item  \n1_login\n2signup :")
selection_item = int(input("your selection "))
if selection_item == 1:
    pass
elif selection_item == 2:
    User.register()
else:
    print("invalid")

