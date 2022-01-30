n = int(input())
d = {}
for i in range(n):
    s = input().split()
    if s[0] not in d:
        d[s[0]] = s[1:]
    else:
        d[s[0]] += s[1:]
    
for k,v in d.items():
    print(k + ":", end=" ")
    print(*v, sep = ", ")