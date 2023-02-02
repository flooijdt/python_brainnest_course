set1 = {1, 2, 3, 4, 5}
set10 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set20 = {4, 5, 6, 7, 8}

for i in set1:
    for ai in set2:
        if i == ai:
            set10.remove(i)
            set20.remove(ai)

set3 = set10.update(set20)
print(set3)
