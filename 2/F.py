import re
l = input()
p = input()
x = re.fullmatch(r'[0-9A-Za-z!#$%&()*+,-./:;<=>?@[\]^_{|}~]{3,32}#\d{4}',l)
if x:
    print('Welcome to Discord')
else:
    print("Invalid password or username")