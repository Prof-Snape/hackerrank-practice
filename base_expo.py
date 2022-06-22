base = int(input("Base = "))
exponent = int(input("Exponent = "))
a = str(base)
b = " *"
c = " " + a + b

print(f"{base} raises to the power of {exponent} is:", base ** exponent, "i.e.", end=(""))
print(f"{c * (exponent - 1)}", a, "=", base ** exponent)
