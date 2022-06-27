# def count_substring(string, sub_string):
#     a = 0
#     for b in range(len(string)):
#         if sub_string in string[b:]:
#             a += 1
#     return a


a = "ablkljojabdwwd"
b = "ab"
c = 0
d = len(a)
print(a[1:])

for i in range(d):
    if a[i:].startswith(b):
        c += 1
print(c)
