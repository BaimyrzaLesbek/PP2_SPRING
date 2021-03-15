n = list(map(int, input().split()))
if sum(n)%4==0:
    print("Kindness")
else:
    print("Greedy")