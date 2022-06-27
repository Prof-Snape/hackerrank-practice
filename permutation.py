from itertools import permutations

string, num = input().split(" ")
b = list(permutations(string, int(num)))
b.sort()

for i in b:
    print("".join(i))
