import re
n = int(input())
for i in range(n):
    s = input().split()
    for j in s:
        x = re.findall(r"[A-Za-z]", j)
        if len(x)%2 == 0:
            print("H", end = " ")
        else:
            print("C", end = " ")
    print()