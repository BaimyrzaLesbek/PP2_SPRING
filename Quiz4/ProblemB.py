import re
s = input()
x = re.fullmatch(r"[A-Za-z0-9_]+",s)
if x:
    print("Found a match!")
else:
    print("Not matched!")
ans = re.finditer