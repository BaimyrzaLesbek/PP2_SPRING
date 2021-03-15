import json
x = '''
{
"Tasks": [ { "name": "Android exam preparation", "priority": "1" }, { "name": "Make tasks for PP2", "priority": "3" }, { "name": "Sleep", "priority": "2" } ]
}
'''
y = json.loads(x)

d = {}

for i in range(len(y["Tasks"])):
    d[y["Tasks"][i]["priority"]]=i
list_keys = list(d.keys())
list_keys.sort()
print(y["Tasks"][d[list_keys[-1]]]["name"])