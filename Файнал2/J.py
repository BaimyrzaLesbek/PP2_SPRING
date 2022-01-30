n = int(input())
d = {}
d1 = {}
d2 = {}
for i in range(n):
    s = input().split()
    if s[0] not in d:
        d[s[0]] = int(s[1])
        d1[s[0]] = 1
    else:
        d[s[0]] += int(s[1])
        d1[s[0]] += 1
for k,v in d.items():
    d2[k]=f'{v/d1[k]:.3f}'

l = sorted(list(d2.values()), reverse=True)
q = []
for i in l:
    for k,v in d2.items():
        if i==v and k not in q:
            q.append(k)
            print(k+":", v)