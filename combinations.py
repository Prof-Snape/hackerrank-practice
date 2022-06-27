from itertools import combinations

string, num = input().split(" ")
a = list(string)
a.sort()
b = []

for i in range(1, int(num) + 1):
    b += list(combinations(a, i))

for i in b:
    print("".join(i))
