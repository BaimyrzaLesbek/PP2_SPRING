s = input().split()
cnt = 0
for i in s:
    if len(i)%2==0:
        cnt+=1
print(cnt)