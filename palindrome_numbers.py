a = int(input())  # ensuring only number gets entered as input
b = str(a)
b = b[::-1]
b = int(b)
print(bool(a == b))

# # method first
# size = len(b)
# c = (size - 1) / 2
# d = b[::-1]
# y = int(0)
#
# while y <= c - 1 and b[y] == d[y]:
#     y += 1
# if y == c:
#     print("true")
# else:
#     print("false")

# # method 2nd
# c = b[::-1]
# d = int(c)
#
# if a == d:
#     print("This is a palindrome.")
# else:
#     print("This isn`t a palindrome.")
#
#
# # method 3rd
# def palindrome(num):
#     s = str(num)
#     e = s[::-1]
#     x = int(s)
#     ys = int(e)
#     if x == ys:
#         print("This is a Palindrome.")
#     else:
#         print("This isn`t a palindrome.")


# palindrome(int(input("Enter numbers: ")))
