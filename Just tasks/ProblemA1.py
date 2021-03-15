import re
s = input()
x = re.search(r"\d{2}BD\d{6}",s)
if x:
    print(x.group(),x.start())
else:
    print("Not Found!")