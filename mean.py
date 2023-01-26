from statistics import mean
# try:
inputs = []
inputo = ""

while inputo != "done":
    inputo = input("Enter a number: ")
    inputs.append(float(inputo))
    if inputo == "done":
        break

print(sum(inputs), len(inputs), mean(inputs))
# except ValueError:
# print("Wrong value!")


# counter()
