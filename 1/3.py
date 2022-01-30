n = int(input())
x = 1
for i in range(n):
    if n <= 0:
        break
    else:
        n -= x
    if n >= 5:
        x += 1
    n -= 1
print(x)