import math
def Prime(a):
    for i in range(2, a):
        if a%i == 0:
            return True
    return False
s = list(map(int, input().split()))
k = list(map(int, input().split()))
l = []
for i in s:
    if Prime(i) and k.count(i)>=1 and i not in l:
        l.append(i)
        print(i, end= " ")