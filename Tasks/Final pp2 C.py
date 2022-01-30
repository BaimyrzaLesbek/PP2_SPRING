a,b = list(map(int, input().split()))
c,d = list(map(int, input().split()))
if a+d >c+b or (a+d==c+b and d>b):
    print("Barsenal")
    print(a+d,c+b)
if a+d < c+b or(a+d==c+b and d<b):
    print("Arselona")
    print(a+d,c+b)
if a+d == c+b and a==c and b==d:
    print("Friendship")
    print(a+d,c+b)