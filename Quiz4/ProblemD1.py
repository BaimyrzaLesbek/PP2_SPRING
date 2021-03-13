f = open('input.txt', 'r')
text = f.readlines()
d = {}
cnt = 0

b=[]

for i in text:
    b.append(i.strip("\n"))

for i in b:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
c=[]

for k,v in d.items():
    if v%2==0:
        c.append(k)

c.sort()
for i in c :
    print(i)
# for i in namesdict:
#     if namesdict[i]%2==0:
#         print()