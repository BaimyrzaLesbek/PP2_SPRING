s = list(map(int, input().split()))
d = {}
for i in range(len(s)):
    d[s[i]]=s.count(s[i])
set1 = set(d.values())
if len(d.values())==len(set1):
    print("Perfect")
else:
    print("Not perfect")