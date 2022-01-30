a = list(map(int, input().split()))
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

s = sorted(list(d.values()))
for k,v in d.items():
    if s[-1] == v:
        print(v)