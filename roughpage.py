a = input()
a += " "
b = []
c = ""

for i in range(len(a)):
    if a[i].isnumeric():
        c += "".join(a[i])
    elif not a[i].isnumeric():
        if len(c) > 0:
            c = int(c)
            b.append(c)
            c = ""

for j in b:
    print(j)
