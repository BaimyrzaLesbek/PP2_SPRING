import re

pattern = '^a...s$'
test_string = 'adsds'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")