s = list(map(int, input().split()))
d = []
for i in range(1,s[0]):
    if s[0]%i==0:
        d.append(i)
d.sort(reverse=True)
for i in range(len(d)):
    if i==s[1]-1:
        print(i)
        exit()