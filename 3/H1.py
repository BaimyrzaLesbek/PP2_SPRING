n = int(input())
for i in range(n):
    s = input().split()
    total = 0
    a = []
    for j in s:
        a.append(len(j))
        total += len(j)
    a.sort()
    print(*a,end=" ")
    print("total: " + str(total))
