a = int(input())
b = int(input())
for i in range(0,b+1):
    if(a<=i*i and i*i<=b):
        print(i*i, end=" ")