# 2. Write a lambda function that takes a list of dictionaries and
# returns a new list of dictionaries sorted by a specified key.

list_o_dicts = [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}]

lista = list(filter(lambda x: x == "a" or x == "d", list_o_dicts))

print(lista)
