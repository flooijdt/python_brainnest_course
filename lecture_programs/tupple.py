def most_common(tupple):
    counts = 0
    list(tupple)
    for i in tupple:
        if tupple.count(i) > counts:
            counts = tupple.count(i)
            item = i
    return item


testtupple = (1, 1, 2, 3, 4, 5)
tupple2 = (1,2,3,5,5,5,6,7,8)
print(most_common(tupple2))
