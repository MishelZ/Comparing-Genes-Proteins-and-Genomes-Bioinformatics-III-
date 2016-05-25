'''
    DPCHANGE(money, Coins)
     MinNumCoins(0) = 0
     for m = 1 to money
        MinNumCoins(m) = inf
            for i = 1 to |Coins|
                if m less then or equal coini
                    if MinNumCoins(m - coini) + 1 less then MinNumCoins(m)
                        MinNumCoins(m) = MinNumCoins(m - coini) + 1
    output MinNumCoins(money)
'''	

def dynamicCoinChange( coins, change ):
	#initialize to zero
    Optimal = [0 for i in range(0, change+1)]
	
    for i in range(1, change+1):
        smallest = float("inf")
        for j in range(0, len(coins)):
            if (coins[j] <= i):
                smallest = min(smallest, Optimal[i - coins[j]]) 
            Optimal[i] = 1 + smallest 
    return Optimal[change]


change = 40;
coins = '50,25,20,10,5,1';
#splitting on comma and map to int
coins = map(int,coins.split(','));

#for coins, change in problems:

print "Minium number of coins=", dynamicCoinChange(coins, change)
