n = int(input())
s = list(map(int, input().split()))
k = int(input())
l = []
for i in range(k):
    d = list(map(int, input().split()))
    cnt = 0
    for j in s:
        if j in range(d[0],d[1]+1):
            cnt += 1
    l.append(cnt)
print(*l, sep="\n")
