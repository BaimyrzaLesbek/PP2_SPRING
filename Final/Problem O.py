s = input()
s = s.upper()
s = s.split()
d = {}
for i in s:
    cnt = s.count(i)
    d[i] = cnt
l = sorted(d.values())
for k,v in d.items():
    if l[-1]==v:
        print(k)