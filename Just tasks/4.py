d = input()
s = d.split()
import re
names = []
dom = []
suf = []
for i in s:
    x = re.fullmatch(r'[0-9a-zA-Z_]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,4}',i)
    if not x:
        continue
nicknames = re.findall(r'([0-9a-zA-Z_]+)@',s)
domain = re.findall(r'@([0-9a-zA-Z]+)\.',s)
suffix = re.findall(r'\.([a-zA-Z]{2,4})',s)
if nicknames: names.append(nicknames[0])
if domain: dom.append(domain[0])
if suffix: suf.append(suffix[0])
names.sort()
dom.sort()
suf.sort()
print("nicknames:")
print(*names,sep = " ")
print("domain name:")
print(*dom, sep = " ")
print("suffix:")
print(*suf,sep = " ")