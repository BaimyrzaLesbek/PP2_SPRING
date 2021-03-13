k = int(input())
s = list(map(int, input().split()))
s1 = set(s)
if(len(s)==len(s1)):
    print("YES")
else:
    print("NO")