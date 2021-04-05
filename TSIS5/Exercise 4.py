f = open('1.txt', 'r')
i = int(input())
data = f.readlines()
d = len(data)-i
print(d)
