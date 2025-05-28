x = [15, 12,  8,  8,  7,  7,  7,  6, 5,  3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n

numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
denominator = (sum((xi - mean_x)**2 for xi in x) * (sum((yi - mean_y)**2 for yi in y)))**0.5

PCC = numerator / denominator

print(round(PCC, 3))
