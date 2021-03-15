import re
s = input()
x = re.fullmatch(r"pp2_midterm_kabdiyev_g2_\d+@[A-Za-z0-9]{1,8}",s)
if x:
    print("Found a match!")
else:
    print("Not matched!")