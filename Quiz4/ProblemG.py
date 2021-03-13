n = int(input())
words = []
common_characters = []
characters = set()
for i in range(n):
    s = input()
    for j in s:
        characters.add(j)
    words.append(characters)
    if len(words)==2:
        c = words[0].intersection(words[1])
    elif len(words)>2:
        c = c.intersection(characters)
    characters = set()
# c = words[0].intersection(words[1],words[2])
# for i in range(len(words)):
#     for j in range(i+1, len(words)):
#         c = words[i].intersection(words[j])
#print(c)
list_characters = list(c)
list_characters.sort()
if list_characters:
    for i in list_characters:
        print(i, end=" ")
else:
    print("NO COMMON CHARACTERS")