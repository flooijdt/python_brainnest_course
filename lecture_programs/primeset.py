set1 = [1,2,3,4,5,6,7,8,9]
primes = set()
# Why it says when remove(i): i dont exist?
# for i in set1:
#     if i != 1 and i != 2:
#         for j in range(2,i):
#             if i % j == 0:
              # set2.remove(i)

def is_prime(n):
    prime = True
    if n != 1:
        for i in range(2,n):
            if n % i == 0:
                prime = False
    return prime

for i in set1:
    if is_prime(i):
        primes.add(i)
print(primes)