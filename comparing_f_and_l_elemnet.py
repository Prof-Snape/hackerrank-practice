x = [10, 20, 30, 40, 10]
y = [75, 65, 35, 75, 30]

# print("Given list:", x)
# print("result is", bool(x[0] == x[-1]))
#
# print("Given list:", y)
# print("result is", bool(y[0] == y[-1]))


def comp(num):
    print(f"Current list is {num}")
    f_num = num[0]
    l_num = num[-1]
    if f_num == l_num:
        print("result is true.")
    else:
        print("result is false.")


# y = [75, 65, 35, 75, 30]
comp(y)
comp(x)
