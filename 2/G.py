a = int(input())
for i in range(a):
    s1 = set(input().split())
    s2 = set(input().split())
    s3 = s1.difference(s2)
    s4 = s2.difference(s1)
    print("Absent:",*sorted(list(s3)), sep=" ")
    print("Lost:",*sorted(list(s4)),sep = " ")