n = int(input())
d = list(map(int, input().split()))
for i in d:
    if d.count(i)==1:
        print(i)
        break