s = list(map(int, input().split()))
l = ""
cnt = 0
for i in s:
    if i != 0:
        l += str(i) + " "
    else:
        cnt += 1
for i in range(cnt):
    l += "0 "
print(l)