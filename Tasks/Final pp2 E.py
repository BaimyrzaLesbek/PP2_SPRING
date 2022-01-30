import re
s = input()
x = re.fullmatch(r'[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]+', s)
if x:
    print("yes")
else:
    print("no")