from itertools import permutations

string, num = input().split(" ")
b = list(permutations(string, 2))
b.sort()

for i in b:
    print("".join(i))
