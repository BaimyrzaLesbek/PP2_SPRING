a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = int(input())
cnt = 0
z = list(zip(a,b))
for i in z:
    if t in range(sum(i)):
        cnt+=1
print(cnt)