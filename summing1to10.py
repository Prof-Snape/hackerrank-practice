t_sum = int()
p_num = int()
for a in range(0, 11):
    t_sum = t_sum + a
    p_num = a
    c = a + p_num
    print(f"Current Number: {a:2} Previous Number: {p_num:2} Sum of Current & Previous Num: {c:2} Sum of all previous "
          f"num: {t_sum:2}")
