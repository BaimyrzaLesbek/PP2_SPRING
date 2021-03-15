f = open('input.txt','r')
text = f.readlines()
cnt = 0
for i in range(len(text)-1):
    if text[i]<text[i+1]:
        cnt += 1
if cnt == len(text)-1:
    print("YES")
else:
    print("NO")