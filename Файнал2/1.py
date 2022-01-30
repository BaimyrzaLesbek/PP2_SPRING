a = int(input())
d = []
for i in range(a):
    s = int(input())
    d.append(s)
k = list(map(int, input().split()))
cnt = 0
for i in d:
    if i%k[0]==0 and i%k[1] != 0:
        print(i)
    else:
        cnt+=1
if cnt==a:
    print(-1)