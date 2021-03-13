import re
txt = input()
t = input()
s = input()
f = input()
x = re.sub(t,s,txt)
d = re.findall(f,x)
print(len(d))