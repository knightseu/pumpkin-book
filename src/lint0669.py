import sys

def coin_change(coins: [], total):
    coins.sort()
    # print(coins[-1])
    a = [sys.maxsize for i in range(total)]
    for coin in coins:
        a[coin-1] = 1
    print(a)
    # Done with init

    for i in range(coins[-1], total):
        min_val = a[i]
        for coin in coins:
           min_val = min(a[i-coin]+1, min_val)
        a[i] = min_val
    
    print("minum number of coins: ", a[-1])
    pass

coin_change([5, 2, 7], 27)
