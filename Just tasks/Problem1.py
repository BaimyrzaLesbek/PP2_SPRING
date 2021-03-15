import re
a = input()
x = re.search(r"(?P<year>.+)\s(?P<month>.+)\s(?P<day>.+)",a)
a = True
if int(x.group("year")) < 1299 or int(x.group("year")) > 1922:
    a = False
elif int(x.group("month")) < 1 or int(x.group("month")) > 12:
    a = False
elif int(x.group("day")) < 1 or int(x.group("day")) > 31:
    a = False
elif len(x.group("month")) != 2 or len(x.group("day")) != 2:
    a = False
if a:
    print("Yes")
else:
    print("NO")