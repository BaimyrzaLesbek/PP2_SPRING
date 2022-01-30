n = int(input())
d = {}
for i in range(n):
    k = list(map(int, input().split()))
    cnt = k.count(1)
    d[i] = cnt
l = sorted(list(d.values()))
m = []
for i in l:
    for k,v in d.items():
        if i == v:
            if k not in m:
                m.append(k)
q = int(input())
print(m[0:q])
