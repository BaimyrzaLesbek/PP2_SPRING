def Prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

s = list(map(int, input().split()))
d = []
for i in range(s[0],s[1]):
    if Prime(i) and i!=1:
        d.append(i)
d = sorted(d, reverse=True)
print(*d, sep=" ")   