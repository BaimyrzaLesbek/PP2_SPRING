n ,m = int(input()),int(input())
k = int(input())
if k % min(m,n) == 0:
    d = min(m,n)
else:
    print("NO")
    exit()
s = 0
for i in range(0,m*n+1,d):
    s += d
    if s==k:
        print("YES")
        exit()
print("NO")