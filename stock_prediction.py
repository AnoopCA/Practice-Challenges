import sys

def printTransactions(m, k, d, name, owned, prices):
    result_list = []
    for i in range(k):
        if owned[i] == 0:
            if int(prices[i][-1]) < m:
                owned[i] = 1
                result_list.append([name[i], 'BUY', owned[i]])
                m = m - (owned[i] * prices[i][-1])
            else:
                owned[i] = 0
                result_list.append([name[i], 'BUY', owned[i]])
        else:
            result_list.append([name[i], 'SELL', owned[i]])
            m = m + (owned[i] * prices[i][-1])
            owned[i] = 0
    print(result_list)

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
