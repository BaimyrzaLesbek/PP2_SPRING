import re
s = input()
a = input()
x = re.search(a,s)
if x:
    print("First time",a,"occured in position:",x.start())
else:
    print("Not found")