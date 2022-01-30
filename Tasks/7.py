s = input().split("-")
m = []
for i in s:
    if len(i)%2 == 0:
        m.append(i)
print(*sorted(m), sep=" ")