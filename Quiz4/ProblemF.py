n = int(input())
s = input()
news = ""
# for i in range(len(s)):
#     s[i] = 'A'
# print(s)
for i in range(n):
    for j in range(len(s)):
        if s[j]=='Z':
            news += 'A'
        else:
            news += chr(ord(s[j])+1)
    s = news
    news = ""
print(s)
# for i in s:
#     ordlist.append(ord(i))
# for i in ordlist:
#     news += chr(i)
# print(news)