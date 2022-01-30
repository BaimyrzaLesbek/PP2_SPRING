s = input().split()
d = {}
for i in s:
    cnt = s.count(i)
    d[i] = cnt
l = sorted(d.keys())
for i in l:
    for k,v in d.items():
        if i==k:
            print(k,v)