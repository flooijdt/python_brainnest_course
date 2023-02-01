def freq(tupple):
    list(tupple)
    dictio = {}
    for i in tupple:
        dictio.update({i: tupple.count(i)})
    return dictio

testtupple = (1, 1, 1, 2, 3, 4)
print(freq(testtupple))
