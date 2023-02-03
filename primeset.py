set1 = [1,2,3,4,5,6,7,8,9]
set2 = [1,2,3,4,5,6,7,8,9]

for i in set1:
    if i != 1:
        for j in range(2, i-1):
            if (i % j) == 0:
                set2.remove(i-1)

print(set2)
