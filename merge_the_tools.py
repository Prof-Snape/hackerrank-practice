def merge_the_tools(string, k):
    new_word_count = len(string) // k
    new_word_list = []
    start_position = 0
    for i in range(new_word_count):
        new_word = string[start_position:start_position + k]
        new_word_list.append(new_word)
        start_position += k

    for i in range(new_word_count):
        required_word = ""
        for j in new_word_list[i]:
            if j not in required_word:
                required_word += j
        new_word_list.append(required_word)

    new_word_list = new_word_list[new_word_count:]
    for i in new_word_list:
        print(i)


if __name__ == '__main__':
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)
