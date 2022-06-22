string = "pynative"
print(string[3:])


def remover(word, n):
    print("Original word: ", word)
    s_word = word[n:]
    print("Sliced Word: ", s_word)


remover("pynative", 4)
remover(input("Word:"), int(input("Num: ")))
