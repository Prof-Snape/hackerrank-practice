"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.
URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true """

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    arr.reverse()
    for i in arr:
        if i < arr[0]:
            print(i)
            break
