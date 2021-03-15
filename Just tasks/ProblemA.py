n = int(input())
d = []
for i in range(n):
    s = list(map(int, input().split()))
    d.append(s)
int1 = int(input())
#count_of_ones = {}
summa = {}
for i in range(len(d)):
    print(sum(d[i]))
    summa[sum(d[i])]=i

print(summa)

# for i in range(len(d)):
#     for j in range(len(d[i])):
#         if d[i][j]==1:
#             if i not in count_of_ones:
#                 count_of_ones[i] = 1
#             else:
#                 count_of_ones[i] += 1

# list_values = list(summa.values())
# list_values.sort()
# keys = []
# for i in list_values[0:int1]:

# print(keys)