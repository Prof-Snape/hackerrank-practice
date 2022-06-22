a = int(input("Enter a number: "))
for x in range(1, a + 1):
    for q in range(0,x):
        print(f"{x} ", end="")
    print()

for x in range(1, a + 1):
    y = str(x)
    z = str(" ")  # adding space after numeric
    p = y + z
    print(p * x)
