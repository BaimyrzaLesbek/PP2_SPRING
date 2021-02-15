a = list(map(int, input().split()))
for i in range(len(a)):
    if(a[i]==0):
        j=i+1
        for j in range(len(a)):
            if a[j]!=0:
                t=a[i]
                a[i]=a[j]
                a[j]=t
                break
for i in a:
    print(i, end=" ")