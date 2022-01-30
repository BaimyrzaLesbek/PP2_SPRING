def po(a):
    k = 2
    while True:
        k*=2
        if k==a:
            return True
        if k>a:
            return False

s = input().split()
d = []
for i in s:
    cnt = s.count(i)
    if cnt==1 and not po(int(i)):
        d.append(int(i))
d.sort()
print(*d, sep = " ")