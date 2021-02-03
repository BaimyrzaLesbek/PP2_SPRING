#This is does not working
a = int(input())
s = 0
for i in range(a+1):
    if i!=0 and a%i==0:
        s+=1
print(s)