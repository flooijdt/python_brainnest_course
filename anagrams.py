lista = ["eat", "tea", "tan", "ate", "nat", "bat"]
lista2 = []
lista3 = []
lista4 = []
lista5 = []
for i in lista:
    lista2.append(list(i))
    lista3.append(sorted(list(i)))
    lista5.append(set(list(i)))
for i in lista2:
    if lista3.count(sorted(i)) > 1:
        lista4.append("".join(i))
print(sorted(lista5))
