n = int(input())
Countries = {}
for i in range(n):
    s = input().split()
    Cities = s[2:]
    Countries[s[0]]=Cities

k = int(input())
for i in range(k):
    city = input()
    flag = True
    for k,v in Countries.items():
        if city in v:
            print(k)
            flag = False
            continue
    if flag:
        print("Unknown")

# "Countries"
# {
#     "Kazakhstan": ["Kyzylorda", "Karaganda", "Uralsk"],
#     "Usa": ["California", "Berkly", "New-york"],
#     "England": ["London"]
# }