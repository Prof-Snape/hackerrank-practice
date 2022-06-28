x = []
a = int(input())
for i in range(1, a + 1):
    b, c = input().split()
    b = int(b)
    c = int(c)
    d = b * c
    x.append(d)

for y in x:
    print(y)
