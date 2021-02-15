a=list(map(int,input().split()))
m=1000000
for i in a:
    if m>i and i>0:
        m=i
print(m)