d = {}
n = int(input())
for i in range(n):
    b = list(input().split())
    d[b[0]] = b[2:]
m = int(input())
t = []
for i in range(m):
    c = input()
    t.append(c)
for c in t:
    flag = True
    for k, v in d.items():
        if c in v:
            print(k)
            break
    else:
        print('Unknown')