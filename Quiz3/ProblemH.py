n = int(input())
s1 = input().split()
k = int(input())
s2 = input().split()
s4 = set(s1)
s5 = set(s2)
s3 = s4.intersection(s5)
solist1 = []
solist2 = []
print("Missed students:")
for i in s1:
    if i not in s3:
        solist1.append(i)
for i in solist1:
    print("-",i)
print("Not in the group:")
for i in s2:
    if i not in s3:
        solist2.append(i)
for i in solist2:
    print("-",i)