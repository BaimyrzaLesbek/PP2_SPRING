import re
x = input()
f = re.findall(r"[02468]+\b",x)
print(*f,sep= ' ')