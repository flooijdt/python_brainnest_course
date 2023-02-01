def unique(tupplaa):
    tupplaa = list(tupplaa)
    lista1=[]
    for i in tupplaa:
        if tupplaa.count(i) == 1:
            lista1.append(i)
            
    return lista1

testtupple = (1,1,2,2,3,3,4)

print(unique(testtupple))
