def rec_divisor(a):
    m = []
    if a==1:
        return 1
    for i in range(1,a):
        if a%i == 0:
            m.append(i)
    return len(m)+rec_divisor(m[-1])


n = int(input())
print(rec_divisor(n))
