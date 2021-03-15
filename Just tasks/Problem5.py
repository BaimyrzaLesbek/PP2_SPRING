s = input()
c = input()
word = []
index = []
for i in range(len(s)):
    word.append(s[i])
    if s[i]==c:
        index.append(i)
