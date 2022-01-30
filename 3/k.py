s1 = set(map(int,input().split()))
s2 = set(map(int,input().split()))
s3 = list(s1.symmetric_difference(s2))
print(*sorted(s3), sep=" ")