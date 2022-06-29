a = ["63 32 2"]
b = []
w = 0

a1 = str(*a)

for i in range(len(a1)):
    if a1[i] == " ":
        w1 = int(a1[w:i])
        b.append(w1)
        w = i + 1

w1 = int(a1[w:len(a1)])
b.append(w1)

b.sort()
print(b)
