d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}
s = input()
for i in s:
    for k,v in d.items():
        if i in v:
            cnt = 0
            for j in range(len(v)):
                if i == v[j]:
                    cnt = j+1
            for j in range(cnt):
                print(k,end="")








