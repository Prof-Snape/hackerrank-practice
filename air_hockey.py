# Alice is playing Air Hockey with Bob. The first person to earn seven points wins the match. Currently,
# Alice's score is A and Bob's score is B.
# Charlie is eagerly waiting for his turn. Help Charlie by calculating the minimum number of points that will be
# further scored in the match before it ends.

#  URL: https://www.codechef.com/submit/AIRHOCKEY

result = []

test_case = int(input())

for i in range(test_case):
    score = [int(x) for x in input().split()]
    score.sort()
    case_result = 7 - score[1]
    result.append(case_result)

for x in result:
    print(x)
