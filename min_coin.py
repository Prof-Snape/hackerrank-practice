# URL: https://www.youtube.com/watch?v=HWW-jA6YjHk
# Cashier have some available coins of different denominations and he/she have to return money to customer. Find the
# minimum numbers of coins cashier will need to return.

def min_coin(cents):
    min_no_coins = 0
    cents = cents % 100     # 100 cents makes 1 dollar.
    for i in denomination_of_available_coins:
        min_no_coins += cents // i
        cents = cents % i
    return min_no_coins


denomination_of_available_coins = [1, 25, 10, 5]
cents_to_return = 56
denomination_of_available_coins.sort(reverse=True)

print(min_coin(cents_to_return))
