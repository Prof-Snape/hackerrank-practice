from itertools import combinations_with_replacement

string, num = input().split(" ")
string = list(string)
string.sort()

b = list(combinations_with_replacement(string, int(num)))

for i in b:
    print("".join(i))
