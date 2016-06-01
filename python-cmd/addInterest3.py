# addinterest3.py
# Kevin Kredit

def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[1] * (1+rate)

def test():
    amounts = [1000, 2200, 800, 360]
    rate = 0.05
    amount = addInterest(amounts, rate)
    print amounts

test()
    
