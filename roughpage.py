a = "aa bbbb cccc afak dasd dasd das 12e"

for x in range(len(a)):
    if a[x] == " ":
        b = a[0:x]
        b = b.capitalize()
        break

for i in range(len(a)):
    if a[i] == " ":
        c = a[i+1:]
        c = c.capitalize()
        for x in range(len(c)):
            if c[x] == " ":
                c = c[:x]
                break
        b += " " + c

print(b)
