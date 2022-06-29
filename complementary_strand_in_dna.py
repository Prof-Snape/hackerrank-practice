# You are given the sequence of Nucleotides of one strand of DNA through a string S of length N. S contains the
# character A, T, C, and G only.
# Chef knows that:
# A is complementary to T.
# T is complementary to A.
# C is complementary to G.
# G is complementary to C.
# Using the string S, determine the sequence of the complementary strand of the DNA.

# URL = https://www.codechef.com/submit/DNASTRAND

result = []

test_case = int(input())

for i in range(test_case):

    length_of_dna = int(input())
    dna = input()
    complementary_dna = ""

    for j in range(length_of_dna):
        if dna[j] == "A":
            complementary_dna += "T"
        elif dna[j] == "T":
            complementary_dna += "A"
        elif dna[j] == "C":
            complementary_dna += "G"
        elif dna[j] == "G":
            complementary_dna += "C"
        else:
            complementary_dna = "Invalid DNA!\n\tCase Sensitive."
            break

    result.append(complementary_dna)

for x in result:
    print(x)
