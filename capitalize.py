def solve(s):
    for x in range(len(s)):
        if s[x] == " ":
            b = s[0:x]
            b = b.capitalize()
            break

    for i in range(len(s)):
        if s[i] == " ":
            c = s[i + 1:]
            c = c.capitalize()
            for x in range(len(c)):
                if c[x] == " ":
                    c = c[:x]
                    break
            b += " " + c
    return b


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
