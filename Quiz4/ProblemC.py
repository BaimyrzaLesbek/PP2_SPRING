# a=int(input())
# for i in range(len(a)):
#     if a[i]>a[i+1]:
#         b=a.reverse(a[i],a[i+1])
# print(i, b)
a = int(input())
b = list(map(int, input().split()))
s = set(b)
b = list(s)
b.sort()
for i in range(len(b)):
    print(i+1,b[i])
