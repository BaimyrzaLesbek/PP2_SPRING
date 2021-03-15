n = list(map(int, input().split()))
cnt = 0
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i]==n[j]:
            cnt += 1
print(cnt)