hours = input("Please, Enter the Hours: ")
rate = input("Please, enter rate: ")

hours = float(hours)
rate = float(rate)


def payment(hours, rate):
    if hours > 40:
        print("Pay: " + str((1.5 * (hours - 40)) + (40 * rate)))
    else:
        print("Pay: " + str(hours * rate))


payment(hours, rate)
