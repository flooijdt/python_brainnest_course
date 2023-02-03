def valuer(lista):
    greater = 0
    for i in lista:
        if i is int:
            greater = i
    for i in lista:
        try:
            if i > greater:
                greater = i
            else:
                continue
        except ValueError:
            continue
    return greater

lista = [1,2,3,4,5,"a",9,"b",6]
print(valuer(lista))