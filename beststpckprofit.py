prices = [10, 7, 5, 4, 1]
min_price = prices[0]
max_profit = float('-inf')

for price in prices[1:]:
    profit = price - min_price

    if profit > max_profit:
        max_profit = profit


    if price < min_price:
        min_price = price

print(max_profit)
