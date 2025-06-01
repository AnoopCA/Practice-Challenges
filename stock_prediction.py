import sys

def printTransactions(m, k, d, name, owned, prices):
    actions = []

    for i in range(k):
        current_price = prices[i][-1]
        if owned[i] > 0 and current_price > prices[i][-2]:
            actions.append(f"{name[i]} SELL {owned[i]}")
            m = m + (current_price*owned[i])
        elif owned[i] == 0 and current_price < prices[i][-2] and m >= current_price:
            buy_amount = int(m // current_price)
            if buy_amount > 0:
                actions.append(f"{name[i]} BUY {buy_amount}")
                m = m - (current_price*buy_amount)
    print(len(actions))
    for action in actions:
        print(action)
    
    print(f'm: {m}')

if __name__ == "__main__":
    data = sys.stdin.read().strip().split('\n')
    lst = []
    for i in data:
        lst.append(i.split())
    m = float(lst[0][0])
    k = int(lst[0][1])
    d = int(lst[0][2])
    
    name = []
    owned = []
    prices = []
    for i in range(1, k+1):
        name.append(lst[i][0])
        owned.append(int(lst[i][1]))
        prices.append(list(map(float, lst[i][2:])))
    
    printTransactions(m, k, d, name, owned, prices)
