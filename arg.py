def fun(**args):
    print(args)

l = [
"24.12.2003",
"28.03.2004",
    ]
for i in l:
    k = i.split(".")
    year = k[2]
    month = k[1] if len(k[1])==2 else "0"+k[1]
    day = k[0] if len(k[0])==2 else "0"+k[0]
    com = f"{year}-{month}-{day}"
    print(com)

