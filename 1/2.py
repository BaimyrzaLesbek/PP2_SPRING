n = int(input())
s = list(map(int, input().split()))
if not s:
    print(0)
else:
    s1 = sorted(s)
    s2 = list(i for i in range(s1[0],s1[0]+n))
    cnt = 0
    for i in s2:
        if i not in s1:
            cnt += 1
    print(cnt)