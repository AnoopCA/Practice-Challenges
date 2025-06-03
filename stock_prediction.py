import sys

def printTransactions(m, k, d, name, owned, prices):
    actions = []
    slopes = []
    for i in range(k):
        x = list(range(len(prices[i])))
        y = prices[i]
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        numerator = sum((x[j]-mean_x)*(y[j]-mean_y) for j in range(n))
        denominator = sum((x[j]-mean_x)**2 for j in range(n))
        slope = numerator / denominator
        slopes.append(slope)
    
    min_slope = min(slopes)
    max_slope = max(slopes)
    slopes = [2 * (s - min_slope) / (max_slope - min_slope) - 1 for s in slopes]

    for i in range(k):
        current_price = prices[i][-1]
        if (owned[i] > 0) and (slopes[i] < -0.25) and (current_price>prices[i][-2]):
            actions.append(f"{name[i]} SELL {owned[i]}")
        elif (owned[i] == 0) and (slopes[i] > 0.25) and (m >= current_price) and (current_price<prices[i][-2]):
            buy_count = int(m // current_price)
            if buy_count > 0:
                actions.append(f"{name[i]} BUY {buy_count}")
                m = m - (current_price*buy_count)
        
    print(len(actions))
    for action in actions:
        print(action)
    
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