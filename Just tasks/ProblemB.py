s = input().split("-")
a = []
for i in s:
    if len(i)%2 == 0: a.append(i)
a.sort()
print(*a, end=" ")