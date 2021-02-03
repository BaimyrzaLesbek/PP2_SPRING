# for cycle
a = int(input())
b = int(input())
for i in range(b):
    if i%2==0 and i>=a:
        print(i, end=" ")
if b%2==0:
    print(b)