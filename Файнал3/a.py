n = int(input())
d = {}
for i in range(n):
    s = input().split()
    if s[0] not in d:
        cnt = 1
        d[s[0]] = [int(s[1]),cnt]
    else:
        d[s[0]][0] += int(s[1])
        d[s[0]][1] += 1

for k,v in d.items():
    print(k+": ",end= "")
    print(f'{v[0]/v[1]:.3f}')