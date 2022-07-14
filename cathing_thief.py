# URL: https://www.youtube.com/watch?v=MFkqnGiCCiU

array_0 = ["T", "T", "P", "P", "T", "P"]
k = 2

max_caught = 0
index_thief = -1
index_police = 0
no_of_police = 0
loop_run = 0

for i in array_0:
    if i == "P":
        no_of_police += 1

while not loop_run > no_of_police:

    for i in range(index_police, len(array_0)):
        if array_0[i] == "P":
            index_police = i
            break

    for i in range(index_police - k, index_police + k + 1):
        if i in range(len(array_0)) and i > index_thief:
            if array_0[i] == "T":
                max_caught += 1
                index_thief = i
                break
    index_police += 1
    loop_run += 1

print(max_caught)
