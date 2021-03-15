n = int(input())
list_numbers = []
for i in range(n):
    k = int(input())
    list_numbers.append(k)
print(max(list_numbers)-min(list_numbers))