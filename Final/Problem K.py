def prime(a):
    k = 1
    while k<a:
        k*=2
    if k==a:
        return True
    return False
s = list(map(int, input().split()))
d = []
for i in s:
    if prime(i) and i not in d:
        d.append(i)
d.sort()
print(*d, sep=" ")