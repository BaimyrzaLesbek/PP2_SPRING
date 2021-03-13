s = list(map(int, input().split()))
year = 0
while True:
    if(s[0]>s[1]):
        print(year)
        break
    s[0]*=3
    s[1]*=2
    year+=1

# a=[int(i) for i in input().split()]
# b=a[0]
# c=a[1]
# s=0
# while b<=c:
#     b=b*3
#     c=c*2
#     s+=1
# print(s)
