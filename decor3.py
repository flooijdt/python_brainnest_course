# 3.
# write a function called validate(func), define a wrapper inside,
# see if arguments were not integer, return and error.
# define a function called add(a, b).
# when calling the func add() in the end, if the args are integers return
# the sum, if even one of them in str, return that error you defined in the
# first function.
def validate(func):
    def wrapper(*args):
        for i in args:
            if type(i) != int:
                return "Error!"
            else:
                return


def add(a, b):
    if type(a) == type(b) == int:
        return a + b
    else:
        return "Error!"


add(1, 2)
