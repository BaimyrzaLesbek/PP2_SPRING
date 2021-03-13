n = int(input())
l = list(map(int, input().split()))
clean = 0
dirty = 0
for i in l:
    if i==1:
        dirty = len(l)
        break
else:
    clean = len(l)
print("Clean:" + str(clean))
print("Dirty:" + str(dirty))