def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += (len(string) - i)
        else:
            stuart_score += (len(string) - i)
    if stuart_score == kevin_score:
        print("Draw")
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Kevin", kevin_score)

if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)


