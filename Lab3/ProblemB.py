n = int(input())
k = []
d = []
for i in range(n):
    s = list(map(int, input().split()))
    k.append(s)

sets = set()
for i in k:
    for j in i:
        sets.add(j)
sets1 = set(sets)
if len(sets)==1:
    print(0)

for i in range(len(k)):
    for j in k[i]:
        d.append(j)

d.sort()
print(d[-2])

# copy = k.copy()
# for i in range(len(k)):
#     if k[i].count(k[i][0])==len(k[i]):
#         cnt+=1
# if cnt != len(k):
#     for i in range(len(k)):
#         d.append(max(k[i]))
#     d = set(d)
#     d = list(d)
#     d.sort()
#     print(d[-2])
# else:
#     print(0)