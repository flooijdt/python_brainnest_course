def evens(tupple):
    list(tupple)
    tupple2 = []
    for i in tupple:
        if i % 2 == 0:
            tupple2.append(i)
    tuple(tupple2)
    return tupple2
    

testtupple = (1,2,3,4,5,6,7,8,9)

print(evens(testtupple))
