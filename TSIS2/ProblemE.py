a = str(input())
s = 0
p = 1
for i in a:
    s += int(i)
    p *= int(i)
print(p-s)