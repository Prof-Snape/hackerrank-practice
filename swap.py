def swap_case(s):
    b = ""
    for i in s:
        if i.isupper():
            b += i.lower()
        elif i.islower():
            b += i.upper()
        else:
            b += i
    return b

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
