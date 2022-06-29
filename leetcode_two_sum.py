# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# URL: https://leetcode.com/problems/two-sum/
# TODO: comeback when more fluent with python class.

# If we are sure that elements of array is digits separated by whitespace then a shorter version of the code would be
# to remove line 11 out from comment and put line 13 to line 27 in comment.

# given_array = [int(x) for x in input().split()]

given_array = input()
given_array += " "
given_array_with_int = []
blank_string = ""

for i in range(len(given_array)):
    if given_array[i].isnumeric():
        blank_string += "".join(given_array[i])
    elif not given_array[i].isnumeric():
        if len(blank_string) > 0:
            blank_string = int(blank_string)
            given_array_with_int.append(blank_string)
            blank_string = ""

given_array = given_array_with_int

sum_of_two = int(input())
result = []

for i in range(len(given_array)):
    for x in range(i + 1, len(given_array)):
        if given_array[x] == (sum_of_two - given_array[i]):
            result.append(i)
            result.append(x)
            break
    if len(result) > 0:
        break

print(result)
