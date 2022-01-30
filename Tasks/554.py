import re
s = input()
x = re.search(r'[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]+', s)
if x:
    print("yes")
else:
    print("no")