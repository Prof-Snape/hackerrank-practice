def print_formatted(number):
    l_e = bin(n)
    l_e = str(l_e)
    l_e = l_e.removeprefix("0")
    l_e = l_e.removeprefix("b")
    l_e = len(l_e)

    for a in range(1, number + 1):
        b = int(a)
        b = str(b)
        b = b.rjust(l_e)

        c = oct(a)
        c = str(c)
        c = c[-l_e:]
        c = c.removeprefix("0")
        c = c.removeprefix("o")
        c = c.rjust(l_e)

        d = hex(a)
        d = str(d).upper()
        d = d[-l_e:]
        d = d.removeprefix("0")
        d = d.removeprefix("X")
        d = d.rjust(l_e)

        e = bin(a)
        e = str(e)
        e = e[-l_e:]
        e = e.removeprefix("0")
        e = e.removeprefix("b")
        e = e.rjust(l_e)

        print(b, c, d, e)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
