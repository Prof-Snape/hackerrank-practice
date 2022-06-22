n, m = map(int, input().split())
a = int((n - 1) / 2)
o = int(1)
p = ".|."

for b in range(a):
    print((p * o).center(m,"-"))
    o += 2
print("WELCOME".center(m,"-"))
z = o - 2
for b in range(a):
    print((p * z).center(m,"-"))
    z -= 2
