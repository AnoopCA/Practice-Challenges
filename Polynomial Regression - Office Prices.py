import sys
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def read_input():
    lines = sys.stdin.read().strip().split("\n")
    f, n = map(int, lines[0].split())

    data = []
    for i in range(1, n+1):
        data.append(list(map(float, lines[i].split())))

    data = np.array(data)
    x_train = data[:,:-1]
    y_train = data[:,-1]
    
    t = int(lines[n+1])
    x_test = []
    for j in range(n+2, n+2+t):
        x_test.append(list(map(float, lines[j].split())))
        
    x_test = np.array(x_test)
    return x_train, y_train, x_test

def main():
    x_train, y_train, x_test = read_input()
    
    model = make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
    model.fit(x_train, y_train)
    
    pred = model.predict(x_test)
    
    for i in pred:
        print(f"{i:.2f}")

if __name__ == "__main__":
    main()
