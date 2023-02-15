# 1. Write a lambda function that takes a list of numbers, and returns
# a new list containing only the positive numbers from the original list.
lister = [1,2,3,4,5,-1,-2]
lista = list(filter(lambda x: x > 0, lister))

print(lista)