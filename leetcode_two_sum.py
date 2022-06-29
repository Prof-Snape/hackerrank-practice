# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# URL: https://leetcode.com/problems/two-sum/

a = [int(x) for x in input().split()]
sum_of_two = int(input())

result = []

for i in range(len(a)):
    for x in range(i + 1, len(a)):
        if a[x] == (sum_of_two - a[i]):
            result.append(i)
            result.append(x)
            break
    if len(result) > 0:
        break

print(result)
