a = input()
b = input()
c = input()
d = a+b+c
e = "qwertyuiopasdfghjklzxcvbnm"
q = ""
for i in e:
    if i not in d:
        q += i
print(*sorted(q),sep="")