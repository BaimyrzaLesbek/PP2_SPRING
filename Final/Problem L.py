s = list(map(int, input().split()))
d = {}
for i in range(s[0]):
    k = list(map(int, input().split()))
    cnt = sum(k)
    d[i] = cnt
l = sorted(d.values())
maxi = l[-1]
for k,v in d.items():
    if maxi == v:
        print(k+1)
        exit()