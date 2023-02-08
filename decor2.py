# 2.
# write a function called authorize(func)
# define a wrapper (func inside another func) inside and return
# "Unathorized access" if not authorized.
# define another function to check whether authorized or not. (True or False)
# define the last function named secret_data()
# to say "This is confidential data" if user is authorized.
# By calling secret_data you should see if the data is confidential or
# you will provoke the other function that says "Unauthorized access".

def authorize(func):
    def unauthorized():
        print("Unauthorized")


def checker(arg):
    if arg:
        print("Auth")
    else:
        print("Unauth")


def secret_data(arg):
    if arg:
        print("This is confidential")


@checker
@authorize
secret_data(True)
