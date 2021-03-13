s = input().split()
s0 = ""
for i in s:
    if len(i)>len(s0):
        s0 = i
print(s0)
print(len(s0))