n = int(input())
s = input()
cnt1,cnt2 = 0,0
for i in range(len(s)-1):
    if s[i]=='S' and s[i+1]=='F':
        cnt1 += 1
    if s[i]=='F' and s[i+1]=='S':
        cnt2 += 1
print("YES") if cnt1 > cnt2 else print("NO")