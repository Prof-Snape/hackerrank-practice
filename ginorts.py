string = input()

sorted_str = ""
lowercase = []
uppercase = []
odd = []
even = []

for i in string:
    if i.islower():
        lowercase.append(i)
    elif i.isupper():
        uppercase.append(i)
    elif int(i) % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

lowercase.sort()
uppercase.sort()
odd.sort()
even.sort()

for i in lowercase:
    sorted_str += i
for i in uppercase:
    sorted_str += i
for i in odd:
    sorted_str += i
for i in even:
    sorted_str += i

print(sorted_str)
