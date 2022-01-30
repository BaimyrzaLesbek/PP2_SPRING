s = list(map(int,input().split()))
j = 1
d = []
if s[0]==s[1]==s[2]:
    print(s[0])
for i in range(1, max(s[0],s[1])+1):
    if s[0]%i==0 and s[1]%i==0:
        d.append(i)
for i in range(len(d)):
    if i == s[2]:
        print(d[-i])
        exit()