a = input().split()
b = 0
for i in a:
    for j in a:
        if int(i)==int(j) and i<j:
            b+=1
print(b)