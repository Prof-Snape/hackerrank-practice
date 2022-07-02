"""Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which
adds to a given number S. In case of multiple sub-arrays, return the sub-array which comes first on moving from left to
right. """


def sub_array_sum(arr, n, s):
    arraylist = [-1]

    for i in range(n):
        remaining_array = arr[i:]
        len_0 = len(remaining_array)
        temp_array = []
        pointer = 0
        temp_sum = 0
        while pointer != len_0:
            temp_sum += remaining_array[pointer]
            temp_array.append(pointer + i + 1)
            if temp_sum == s:
                arraylist = [temp_array[0], temp_array[-1]]
                return arraylist
            elif temp_sum > s:
                pointer = len_0
            if pointer < len_0:
                pointer += 1
    return arraylist


array_0 = [1, 2, 23, 27]
na = len(array_0)
sa = 27
call = sub_array_sum(array_0, na, sa)
print(call)
