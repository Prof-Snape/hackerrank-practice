a = "010"
b = "010101111010"
occurrence = 0

for i in range(len(b)):
    if b[i:].startswith(a):
        occurrence += 1

print(occurrence)
