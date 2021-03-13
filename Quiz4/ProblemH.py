s = list(map(int, input().split()))
days = []
average_score = []
flag = True
for i in range(s[0]):
    scores = list(map(int, input().split()))
    days.append(scores)
for i in range(len(days)):
    cnt = 0
    for j in days[i]:
        cnt += j
        average_score.append(cnt//3)

for i in average_score:
    if i>=s[1]:
        print("YES")
        break
else:
    print("NO")



# for i in range(len(days)):
#     for j in days[i]:
#         if s[1] :
#             print("YES")
#             flag = False
#             break
#     if not flag:
#         break
# if flag:
#     print("NO")