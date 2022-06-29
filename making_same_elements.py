# Chef has an array A of length N. In one operation, Chef can choose any two distinct indices i,j (1≤i,j≤N,
# i!=j) and either change A_i to A_j or change A_j to A_i. Find the minimum number of operations required to make
# all the elements of the array equal.

# URL: https://www.codechef.com/submit/PAIREQ?tab=statement

result = []

for x in range(int(input())):

    numbers_of_element = int(input())
    array_being_checked = [int(x) for x in input().split()]
    array_being_checked.sort()

    replace_with = array_being_checked[0]
    occurrence = 1
    previous_occurrence = 1
    var = 0

    for i in range(numbers_of_element - 1):
        if array_being_checked[i] == array_being_checked[i + 1]:
            occurrence += 1
        elif occurrence > previous_occurrence:
            replace_with = array_being_checked[i]
            previous_occurrence = occurrence
            occurrence = 1

    if occurrence > previous_occurrence:
        replace_with = array_being_checked[len(array_being_checked) - 1]

    for i in range(len(array_being_checked)):
        if array_being_checked[i] != replace_with:
            var += 1
    result.append(var)

for i in result:
    print(i)
