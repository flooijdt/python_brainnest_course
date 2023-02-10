username = input("input your username please: ")

while username != "username":
    print("Wrong username!")
    username = input("input your username: ")

password = input("input your password: ")

while password != "password":
    print("Wrong password.")
    password = input("input your password: ")
else:
    print("you are in!")
    