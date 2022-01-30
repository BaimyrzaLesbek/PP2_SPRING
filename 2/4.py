s = input().split()
d = ""
for i in s[0]:
    if i in s[1] and i in s[2] and i not in d:
        d+=i
print(*sorted(d),sep="")