a = input()

# print(any(c.isalnum() for c in a))

for x in a:
    if x.isalnum():
        print(True)
        break
else:
    print(False)
for x in a:
    if x.isalpha():
        print(True)
        break
else:
    print(False)
for x in a:
    if x.isdigit():
        print(True)
        break
else:
    print(False)
for x in a:
    if x.islower():
        print(True)
        break
else:
    print(False)
for x in a:
    if x.isupper():
        print(True)
        break
else:
    print(False)
