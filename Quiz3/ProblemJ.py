import json
a = input()
y = json.loads(a)

# print(y["Subscriptions"][0]["price"])

x = {}
for i in range(len(y["Subscriptions"])):
    d = (int(y["Subscriptions"][i]["price"])*(100-int(y["Subscriptions"][i]["discount"])))//100
    x[d]=i
list_keys = list(x.keys())
list_keys.sort()

print("Name:",y["Subscriptions"][x[list_keys[0]]]["name"])
print("Price:",list_keys[0])