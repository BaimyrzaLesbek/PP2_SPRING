n = int(input())
d = []
for i in range(n):
    s = list(map(int, input().split()))
    d.append(s)
k = tuple(zip(*d))

