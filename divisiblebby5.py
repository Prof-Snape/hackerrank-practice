x = [10, 20, 33, 46, 55]

print("Divisible by 5")
for a in x:
    if a % 5 == 0:
        print(a)

y = []
n = int(input("Number of elements: "))
for a in range(0, n):
    c = int(input(f"Enter element positioned at {a + 1}: "))
    y.append(c)
print(f"Given list: {y}")

print("Divisible by 5")
for a in y:
    if a % 5 == 0:
        print(a)
