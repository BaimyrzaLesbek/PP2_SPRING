n = int(input())
d = {}
for i in range(n):
    s = input().split()
    if s[0] not in d:
        d[s[0]]=[s[1]]
    else:
        if s[1] not in d[s[0]]:
            d[s[0]].append(s[1])

for k,v in sorted(d.items()):
    if len(v)>=3:
        print(k+" +1")
    else:
        print(k+" NO BONUS")