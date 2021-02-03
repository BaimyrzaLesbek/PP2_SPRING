v = int(input())
t = int(input())
s = int((abs(v)*t)%109)
if s==0:
    print(0)
elif v>=0:
    print(s)
else:
    print(109-s)