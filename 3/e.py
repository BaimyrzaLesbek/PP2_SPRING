a = list(map(int,input().split()))
b = sorted(a)
cnt = 0
for i in range(len(a)):
    for j in range(i, len(b)):
        if a[i]!=b[j]:
            cnt += 1
        break
print(cnt)