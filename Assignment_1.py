name = "Salih"
password = "E2031"
user = input("Please enter your first name :")
if user.title() == name:
    print(f"Hello, {user.title()}! The password is : {password}")
else:
    print(f"Hello, {user.title()}! See you later.")
