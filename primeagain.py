def is_prime(n):
    prime = True
    if n != 1:
        for i in range(2,n):
            if n % i == 0:
                prime = False
    return prime

def prime_num(num):
    lst = []
    counter = 0
    for i in range(2, 100):
        if counter < num:
            if is_prime(i):
                lst.append(i)
                counter += 1
            else:
                continue
    print(lst)

prime_num(5)
prime_num(10)