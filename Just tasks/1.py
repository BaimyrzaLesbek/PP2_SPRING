x = input().split()
a = int(input())
setN = set()
for i in range(a):
    n = input().split()
    for j in n:
        setN.add(j)
setO = set()
for i in x:
    if not(i in setN):
        setO.add(i)
print(*(sorted(setO,reverse=True)),sep = " ")