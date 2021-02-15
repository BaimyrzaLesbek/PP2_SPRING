a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = int(0)
for i in a:
    for j in b:
        if i==j:
            c+=1
print(c)