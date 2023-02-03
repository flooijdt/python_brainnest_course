lista = ["list", "o", "strings", "1.2"]
def lister(lista):
    listab = []
    for i in range(len(lista)):
        try:
            listab.append(float(lista[i]))
        except ValueError:
            continue
    return listab

print(lister(lista))
