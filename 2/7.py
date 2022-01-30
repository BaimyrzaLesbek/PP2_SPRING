n = int(input())
l1 = []
l2 = []
l3 = []
d = {}
for i in range(n):
    s = input().split()
    num = list(map(int,s[2:]))
    l3.append(num)
z = list(zip(*l3))
for i in z:
    print(i)
    print(i.count(0))
    if i.count(0)>=n//2:
        for j in i:
            print(j)
            j += 5
    print(i)
print(z)

#     summa = sum(num)
#     if summa>=20:
#         l2.append(summa)
#         d[s[1]]=summa


# for i in reversed(sorted(l2)):
#     for k,v in d.items():
#         if v == i and k not in l1:
#             print(k)
#             l1.append(k)

    # if num[0]==0:
    #     d1["1"]+=1
    # elif num[1]==0:
    #     d1["2"]+=1
    # elif num[2]==0:
    #     d1["3"]+=1
    # elif num[3]==0:
    #     d1["4"]+=1