def print_rangoli(size):
    width = 1 + (size - 1) * 4
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    required_char = alphabet[size - 1::-1]
    upper_half = []

    # upper half of rangoli.
    for i in range(size):
        char = required_char[0:i+1]
        mid_line = ""
        for j in char:
            mid_line += j
            mid_line += "-"
        for j in char[-2::-1]:
            mid_line += j
            mid_line += "-"
        mid_line = mid_line[:-1]
        line = ("-" * ((width - len(mid_line)) // 2) + mid_line + "-" * ((width - len(mid_line)) // 2))
        upper_half.append(line)
        print(line)

    # bottom of rangoli.
    for i in upper_half[-2::-1]:
        print(i)


if __name__ == '__main__':
    n = 5
    print_rangoli(n)
