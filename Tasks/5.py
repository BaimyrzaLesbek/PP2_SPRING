import re
s = input()
x = re.fullmatch(r"PP2.+midterm", s)
if x:
    print("Success")
else:
    print("No")