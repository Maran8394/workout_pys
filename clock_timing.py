s = 8
e = 10
t = []
for i in range(s,12+1):
    t.append(i)
    if i == 12:
        for j in range(1,e+1):
            t.append(abs(j))

print(t)

