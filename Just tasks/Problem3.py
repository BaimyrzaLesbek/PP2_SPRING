s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
k = int(input())
cnt = 0
x = list(zip(s1,s2))
for i in range(len(x)):
    if k in range(sum(x[i])) and k<=x[i][1]:
        cnt += 1
print(cnt)