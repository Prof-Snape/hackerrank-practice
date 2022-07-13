"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
URL: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
"""


def insert_array(array, i, e):
    array.insert(i, e)


def print_array(array):
    print(array)


def remove_array(array, e):
    array.remove(e)


def append_array(array, e):
    array.append(e)


def sort_array(array):
    array.sort()


def pop_array(array):
    array.pop(-1)


def reverse_array(array):
    array.reverse()


if __name__ == '__main__':
    test_case = int(input())
    empty_array = []

    for a in range(test_case):
        request = input().split()
        if request[0] == "insert":
            insert_array(empty_array, int(request[1]), int(request[2]))
        elif request[0] == "print":
            print_array(empty_array)
        elif request[0] == "remove":
            remove_array(empty_array, int(request[1]))
        elif request[0] == "append":
            append_array(empty_array, int(request[1]))
        elif request[0] == "sort":
            sort_array(empty_array)
        elif request[0] == "pop":
            pop_array(empty_array)
        elif request[0] == "reverse":
            reverse_array(empty_array)
