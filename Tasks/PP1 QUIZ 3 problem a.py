#ne resheno
def prime(i):
    if i==1:
        return 2
    cnt = 1
    p = 2
    while True:
        p2 = 2
        if p%p2 == 0:
            p += 1
            cnt += 1
        else:
            p2 += 1
        if cnt==i:
            break
    return p
    
n = int(input())
print(prime(n))