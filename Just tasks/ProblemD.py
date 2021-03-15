list_of_unique_numbers = []
cnt = 0
n = list(map(int, input().split()))
for i in range(len(n)):
    if n.count(n[i])==1:
        list_of_unique_numbers.append(n[i])
print(sum(list_of_unique_numbers))