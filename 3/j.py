import re
s = input()
x = re.fullmatch(r"PP2.+midterm",s,re.IGNORECASE)
if x:
    print("Success")
else:
    print("No")