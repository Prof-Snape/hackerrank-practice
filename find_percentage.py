"""The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of
students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
URL: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true """


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for a in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    total_marks = 0
    for a in marks:
        temp = a
        total_marks += temp
    average_marks = total_marks / len(marks)
    print("{:.2f}".format(average_marks))
