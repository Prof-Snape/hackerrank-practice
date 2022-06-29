# URL: https://www.codechef.com/submit/KTTABLE

result = []

test_case = int(input())

for i in range(test_case):

    no_of_students = int(input())
    finish_time = [int(x) for x in input().split()]
    required_time = [int(x) for x in input().split()]

    result_temp = 0
    allotted_time = []
    temp = [0]
    temp += finish_time[:no_of_students - 1]

    for j in range(no_of_students):
        a = finish_time[j] - temp[j]
        allotted_time.append(a)
        if allotted_time[j] >= required_time[j]:
            result_temp += 1

    result.append(result_temp)

for x in result:
    print(x)
