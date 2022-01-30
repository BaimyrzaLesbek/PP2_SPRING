n = int(input())
d = {}
m = []
for i in range(n):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
    if d[s] >= 2:
        m.append(s)
if m:
    print(*m, sep= "\n")
else:
    print("Understandable, have a great day")