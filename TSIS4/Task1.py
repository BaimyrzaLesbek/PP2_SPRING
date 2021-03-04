import re

f = open('./data.txt', 'r',encoding="utf-8")
data = f.read()

name = re.search(r"Филиал ТОО.+", data)
binn = re.search(r"\d{12}", data)

title = re.findall(r"\d+\.\n(.+)", data)
count = re.findall(r"(\d)\,0{3}", data)
unit = re.findall(r"x\s(.+)\,0{2}", data)
total = re.findall(r"Стоимость\n(.+),0{2}", data)

date = re.search(r"(\d\d.\d\d.\d{4}\s\d\d.\d\d.\d\d)", data)
address = re.search(r"г\..+", data)

print(name.group())
print(binn.group())
for i in range(len(title)):
    print("1. Title: " + title[i])
    print("2. Count: " + count[i])
    print("3. Unit price: " + unit[i])
    print("4. Total price: " + total[i])
print(date.group())
print(address.group())