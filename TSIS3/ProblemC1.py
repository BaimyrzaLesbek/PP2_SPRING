a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list()
for i in a:
    for j in b:
        if i==j:
            c.append(i)
c.sort()
for i in c:
    print(i, end=" ")