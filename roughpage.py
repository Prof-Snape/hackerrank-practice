s = "aaaDSDss"
b = ""

for i in s:
    if i.isupper():
        b += i.lower()
print(b)
