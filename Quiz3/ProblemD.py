moves = input()
a = list(map(int, input().split()))
b = [0,0]
if a==b:
    print("Passed")
else:
    for i in moves:
        if i=='L':
            b[0]-=1
        elif i=='R':
            b[0]+=1
        elif i=='U':
            b[1]+=1
        elif i=='D':
            b[1]-=1
        if a==b:
            print("Passed")
            break
    else:
        print("Missed")