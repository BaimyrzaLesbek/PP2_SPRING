n = int(input())
k = []
d = []
for i in range(n):
    s = list(map(int, input().split()))
    k.append(s)
for i in range(len(k)):
    d.append(max(k[i]))
print(max(d))