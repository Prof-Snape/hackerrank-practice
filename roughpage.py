s = input()
b = ""

for i in s:
    if i.isupper():
        b += i.lower()
    elif i.islower():
        b += i.upper()
    else:
        b += i
print(b)
