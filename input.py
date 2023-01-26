hours = input("Please, Enter the Hours: ")
rate = input("Please, enter rate: ")

hours = float(hours)
rate = float(rate)
try:
    type(hours) != str
except:
    print("you wrote a string!")

if hours > 40:
    print("Pay: " + str(1.5 * hours * rate))
else:
    print("Pay: " + str(hours * rate))
