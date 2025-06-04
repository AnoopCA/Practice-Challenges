import sys
from heapq import heappush, heappop

def printTransactions(m, k, d, name, owned, prices):
    actions = []
    drop = []
    for i in range(k):
        price_move = (prices[i][-1] - prices[i][-2]) / prices[i][-2]
        if price_move > 0 and owned[i] > 0:
            actions.append(f"{name[i]} SELL {owned[i]}")
        elif price_move < 0:
            heappush(drop, (price_move, i, name[i]))

    while m > 0.0 and drop:
        rate, idx, name = heappop(drop)
        buy_count = int(m / prices[idx][-1])
        if buy_count  > 0:
            actions.append(f"{name} BUY {buy_count}")
            m -= buy_count * prices[idx][-1]

    print(len(actions))
    for action in actions:
        print(action)

if __name__ == '__main__':
    data = sys.stdin.read().strip().split('\n')
    lst = []
    for i in data:
        lst.append(i.split())
    m = float(lst[0][0])
    k = int(lst[0][1])
    d = int(lst[0][2])
    
    names = []
    owned = []
    prices = []
    for i in range(1, k+1):
        names.append(lst[i][0])
        owned.append(int(lst[i][1]))
        prices.append(list(map(float, lst[i][2:])))

printTransactions(m, k, d, names, owned, prices)