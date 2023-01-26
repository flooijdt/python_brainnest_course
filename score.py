number = input("Input a number from 0.0 to 1.0: ")

def computegrade(number):
    try:
        float(number)
    except ValueError:
        print("You entered a string!")

    number = float(number)

    if number >= 0.9:
        return "A"
    elif number >= 0.8:
        return "B"
    elif number >= 0.7:
        return "C"
    elif number >= 0.6:
        return "D"
    elif number < 0.6:
        return "F"
    else:
        return("something went wrong.")

print(computegrade(number))
