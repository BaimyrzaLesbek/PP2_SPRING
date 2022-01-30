a = input().split()
cnt = 0
for i in a:
    if a.count(i)==1:
        cnt+=int(i)
print(cnt)