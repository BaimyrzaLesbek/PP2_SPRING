n = int(input())
d = {}
for i in range(n):
    s = input().split()
    if s[0] not in d:
        d[s[0]]=int(s[1])
    else:
        d[s[0]]+=int(s[1])
l = sorted(list(d.values()))
su = sum(l)
for i in reversed(l):
    for k,v in d.items():
        if i==v:
            print(k,str(float('%.4f' % (v/su*100)))+"%")