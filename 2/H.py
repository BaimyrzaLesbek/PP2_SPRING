import re
s = input()
nick = []
dom = []
suf = []
for i in s:
    x = re.match(r"(\w+)@(\w+)\.([a-z]{2,4})",i)
    if x:
        nick.append(x.group(1))
        dom.append(x.group(2))
        suf.append(x.group(3))
print("nicknames:")
print(*nick, sep=" ")

print("domain name:")
print(*dom, sep=" ")

print("suffix:")
print(*suf, sep=" ")