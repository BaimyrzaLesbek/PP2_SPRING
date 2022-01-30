def divisors(x, counter):
    k=0
    if x == 1:
        return counter
    for i in range(1, x):
        if x // i == 0:
            counter += 1
            if i != x:
                k = i
    return divisors(k, counter)


a = int(input())
counter = 0
print(divisors(a, counter))