a = int(input("Enter your taxable income: "))

if a <= 10000:
    print("You owe 0.")
elif a <= 20000:
    print("You owe", ((a-10000)/10)+0)
else:
    print("You owe: ", ((a-20000)/5)+1000)
