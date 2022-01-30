n = int(input())
fuck = []
fuckfuck = []
total = []
for i in range(n):
    fuck.clear()
    a = [str(i) for i in input().split()]
    for j in range(len(a)):
        fuck.append(len(a[j]))
    fuckfuck.append(fuck)
    fuckfuck[i]=sorted(fuckfuck[i])
    total.append(sum(fuckfuck[i]))
for i in range(len(fuckfuck)):
    print(*fuckfuck[i], end = " ")
    print("total: " + str(total[i]))