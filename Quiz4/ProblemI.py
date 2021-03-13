n = int(input())
l = list(map(int, input().split()))
l_sorted = l.copy()
l_sorted.sort()
flag = False
for i in range(len(l)):
    for j in range(i,i+1):
        if l[i] != l_sorted[j]:
            print("Not interesting")
            flag = True
            break
    if flag:
        break
else:
    print("Interesting")



# if l==l_sorted:
#     print("Interesting")
# else:
#     print("Not interesting")