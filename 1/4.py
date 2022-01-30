n = int(input())
s = list(map(int, input().split()))
d = {}
for i in s:
    d[i] = s.count(i)
print(d[1])
cnt = 1
for i in range(1,len(s)-1):
    if s[i] != 1:
        cnt += 1
    else:
        break
k = len(s)
cnt1 = 1
while cnt<k:
    if cnt1==d[1]:
        break
    k -= cnt
    cnt1 += 1
    print(cnt,end = ' ')
print(k)
