a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(a[0],a[1]+1):
    if i not in b:
        print(i,end=" ")