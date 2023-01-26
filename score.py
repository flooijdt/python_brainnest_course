number = input("Input a number from 0.0 to 1.0: ")

try:
    not isinstance(number, str)
except:
    print("You entered a string!")

number = float(number)

if number >= 0.9:
    print("A")
elif number >= 0.8:
    print("B")
elif number >= 0.7:
    print("C")
elif number >= 0.6:
    print("D")
elif number < 0.6:
    print("F")
else:
    print("something went wrong.")
