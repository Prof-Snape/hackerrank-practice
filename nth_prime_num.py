import time

st = time.time()
st_2 = time.process_time()


def prime_number(nth_term):
    natural_num = 1
    n_of_nth_prime = 3

    while n_of_nth_prime != nth_term:
        for i in range(2, natural_num // 2):
            if natural_num % i == 0:
                # print("Not a prime", num)
                break
            if i == natural_num//2 - 1:
                n_of_nth_prime += 1
                print("Prime serial number:", n_of_nth_prime)
                print("Prime number:", natural_num)
                if n_of_nth_prime == nth_term:
                    print(f"{nth_term}th prime numbers is:", natural_num)
        natural_num += 1


prime_number(int(input("Which nth prime number you are looking for?")))

elapsed_time = time.time() - st
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
et = time.process_time()
res = et - st_2
print('CPU Execution time:', time.strftime("%H:%M:%S", time.gmtime(res)))
