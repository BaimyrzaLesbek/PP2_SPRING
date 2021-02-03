a = int(input())
print(str(int(a%86400/3600))+":"+str(int(a%3600/600))+str(int(a%600/60))+":"+str(int(a%60/10))+str(int(a%10)))