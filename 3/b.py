s = sorted(input().split())
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for k,v in d.items():
    print(k+" - "+ str(v))