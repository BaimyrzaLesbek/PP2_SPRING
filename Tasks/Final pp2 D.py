global l
l = list()
def rec(a,b):
    if a==b:
        return a
    if b%2 == 0:
        l.append([False, b])
        return rec(a,b+1)
    l.append([True, b])
    return rec(a,b+1)
    
s = list(map(int, input().split()))
rec(s[1],s[0])
for i in l:
    if i[0]:
        print(i[1], end= " ")
if s[1]%2 != 0:
    print(s[1])