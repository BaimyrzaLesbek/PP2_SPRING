import re
n = int(input())
d = {'a':0,'b':0,'c':0}
for i in range(n):
    s = input().split()
    x = re.findall(r'[A-Z]',s[0])
    d['a']+=len(x)
    y = re.findall(r'[eioauEUIOA]',s[1])
    d['b']+=len(y)
    z = re.findall(r'\d',s[2])
    d['c']+=len(z)
print(d)