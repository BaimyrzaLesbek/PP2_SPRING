n = int(input())
a = []
for i in range(n):
    s = sorted(input())
    if s not in a:
        print(0)
    else:
        print(a.count(s))
    a.append(s)
        