f = open('1.txt', 'r')
i = int(input())
for j in range(i):
    print(f.readline())
f.close()


# f = open('1.txt', 'r')
# data = f.read()
# data = data.split("\n")
# i = int(input())
# cnt = 0
# for j in range(0,i):
#     print(data[j])

# import os

# txt = open('1.txt','r', encoding="utf-8")
# cnt = 0
# for line in txt.readlines():
#     print(line, end="")
#     cnt += 1
#     if(cnt == 6):
#         break