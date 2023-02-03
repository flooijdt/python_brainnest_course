lista = ["eat", "tea", "tan", "ate", "nat", "bat"]
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
for i in lista:
    lista2.append(list(i))
    lista3.append(sorted(list(i)))
    lista5.append(set(list(i)))

for i in lista2:
    if lista3.count(sorted(i)) > 1:
        lista4.append("".join(i))

for i in lista3:
    lista6.append("".join(i))

print(set(lista6))
print(lista)
print(lista2)
print(lista3)
print(lista4)
print(sorted(lista5))
print(lista6)
# print(sorted(lista5))
def separator(setx):
    for i in range(len(setx)):
        if setx[i] == setx[i + 1]:
            