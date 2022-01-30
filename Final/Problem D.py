s = input().split()
l_words = []
for i in s:
    j = i[::-1]
    if i != j:
        if i not in l_words:
            l_words.append(i)
l_words.sort()
for i in l_words:
    print(i)