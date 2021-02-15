# ne resheno
a = int(input())
b = int(input())
a1 = []
b1 = []
for i in range(a):
    s = int(input())
    a1.append(s)
for i in range(b):
    s = int(input())
    b1.append(s)
c = []
d = []
e = []
for i in a1:
    for j in b1:
        if i==j:
            c.append(i)
c.sort()
print(len(c))
for i in c:
    print(c, end=" ")
