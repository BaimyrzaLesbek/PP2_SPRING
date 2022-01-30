import re
def IsPower(q):
    p = 1
    while p<q:
        p*=2
    return p==q
# n = int(input())
# l = []
# for i in range(n):
#     s = input()
#     x = re.findall(r"([A-Za-z]+)\d*([A-Za-z]*)\d*([A-Za-z]*)\d*([A-Za-z]*)\d*([A-Za-z]*)",s)
#     for j in x:
#         l.append(x[0]+x[1]+x[2]+x[3]+x[4])
#     for j in l:
#         if IsPower(len(j)):
#             print("H", sep = " ")
#         else:
#             print("C", sep = " ")


import re
n = int(input())
cnt = 0
list_of_numbers = ['0','1','2','3','4','5','7','8','9']
for i in range(n):
    s = input()
    x = re.findall(r'[A-Za-z0-9]+',s)
    for j in x:
        for k in j:
            if k in list_of_numbers:
                cnt += 1
        if IsPower(len(j)-cnt):
            print("H", sep = " ")
        else:
            print("C", sep = " ")
        cnt = 0