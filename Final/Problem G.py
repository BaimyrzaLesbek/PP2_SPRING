import re
s = input()
s.lower()
s = s.split()
d = {}
char = "abcdefghijklmnopqrstuvwxyz"
for j in char:
    cnt = 0
    for i in s:
        if i[0]==j:
            cnt+=1
    d[j]=cnt
for k,v in d.items():
    print(v)