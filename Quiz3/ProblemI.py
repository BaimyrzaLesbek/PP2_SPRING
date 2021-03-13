n = int(input())
s = list(map(int, input().split()))
k = int(input())
if k==0:
    print(0)
else:
    s1 = ""
    s2 = ""
    for i in range(len(s)):
        if i>=0 and i<=k-1:
            s1 += str(s[i])
        elif i>=k and i<=n-1:
            s2 += str(s[i])
    print(int(s1)*int(s2))