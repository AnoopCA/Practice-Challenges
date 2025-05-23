x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]  # Physics
y = [10, 25,17,11,13,17,20,13, 9,15]  # History

n = len(x)

mean_x = sum(x) / n
mean_y = sum(y) / n

cov_xy = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
var_x = sum((x[i] - mean_x)**2 for i in range(n))

b = cov_xy / var_x

a = mean_y - (b * mean_x)

x_pred = 10
y_pred = a + (b * x_pred)

print(round(y_pred, 1))
