import re
s = input()
x = re.findall(r"[13579]",s)
print(len(x))