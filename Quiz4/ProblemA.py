import re
s = input()
d = re.match
x = re.search(r"[A-Z]+[a-z]+",s)
if x:
    print("Found a match!")
else:
    print("Not matched!")