# There are 1010 problems in a contest. You know that the score of each problem is either 11 or 100100 points.
#
# Chef came to know the total score of a participant and he is wondering how many problems were actually solved by
# that participant.
#
# Given the total score PP of the participant, determine the number of problems solved by the participant. Print -1−1
# in case the score is invalid.

# URL: https://www.codechef.com/submit/ACS

result = []

no_of_testcase = int(input())
for i in range(no_of_testcase):
    points = int(input())
    if (points // 100) + (points % 100) < 11:
        a = (points // 100) + (points % 100)
    else:
        a = -1
    result.append(a)

for i in result:
    print(i)
