# ne reshil
a = list(map(int, input().split()))
for i in range(len(a)):
    if(a[i]==0):
        for j in range(len(a)):
            if a[j]!=0:
                print("a[",i,"]=",a[i])
                print("a[",j,"]=",a[j])
                t=a[j]
                a[j]=a[i]
                a[i]=t
                print("a1[",i,"]=",a[i])
                print("a1[",j,"]=",a[j])
                break
for i in a:
    print(i, end=" ")