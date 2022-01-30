s = input()
d = {}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(len(d))
for k,v in sorted(d.items()):
    print(k, v)