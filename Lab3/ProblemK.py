n = list(map(int, input().split()))
d = []
for i in range(n[0]):
    s = list(map(int, input().split()))
    d.append(s)
for i in range(len(d)):
    print("The sum of row number",i+1,"is",sum(d[i]))
x = list(zip(*d))
summa = 0
for i in range(len(x)):
    for j in x[i]:
        summa += j
    print("The sum of column number",i+1,"is",summa)
    summa = 0