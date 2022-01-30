# s = list(map(int, input().split()))
# l = []
# k = int(input())
# for i in range(1,s[-1]):
#     if i not in s:
#         l.append(i)
# print(l[k-1])

x=list(map(int,input().split()))
y=int(input())
n=max(x)
a=[]
for i in range(1,n+1):
    a.append(i)
for i in x:
    a.remove(i)
print(a[y-1])