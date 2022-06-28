x = []
c = 0
a = int(input())

for i in range(a):
    b = int(input())
    b = str(b)
    for a in b:
        if int(a) == 4:
            c += 1
    x.append(c)
    c = 0

for y in x:
    print(y)
