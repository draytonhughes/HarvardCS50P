# Ask for money on 50 cents to buy a coke.  Can only take .25, .10, and .05

amount_due = 50
coins = [5, 10, 25]

# Creates a loop that keeps this going until it goes past the amount due

while amount_due > 0:
    print(f'Amount Due: {amount_due}')
# Inputs the coin
    coin = int(input('Insert Coin: '))

# Deducts the coin from the normal amount due which is 50
    if coin in coins:
        amount_due -= coin;

# Shows change if you over pay or will print 0
print(f'Change Owed: {abs(amount_due)}')
