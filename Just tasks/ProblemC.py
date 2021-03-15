import re
s = input()
s1 = s.split()
n = int(input())
for i in range(n):
    cnt = []
    slovo = input()
    x = re.findall(r"^("+slovo+")",s)
    print(x) 