list_o_dicts = [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}]

lista = list(filter(
    lambda x: [i for i in x if "a" in i or "d" in i], list_o_dicts))

print(lista)
