n = int(input())
s = list(map(int, input().split()))
j = sorted(s)
for i in s:
    if i != j[-1]:
        print(0, end = " ")
    else:
        print(1 , end= " ")