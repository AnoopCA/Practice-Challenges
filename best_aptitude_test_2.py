import sys
import numpy as np
from scipy.stats import rankdata, spearmanr

def find_best_test(gpa, tests):
    gpa_ranks = rankdata(gpa)
    best_test = -1
    best_corr = -2
    for i in range(5):
        test_scores = tests[i]
        test_ranks = rankdata(test_scores)
        corr, _ = spearmanr(gpa_ranks, test_ranks)
        if corr > best_corr:
            best_corr = corr
            best_test = i + 1
    return best_test

def main():
    input_lines = sys.stdin.read().splitlines()
    #input_lines = ['1', '5', '7.5 7.7 7.9 8.1 8.3', '10 30 20 40 50', '11 9 5 19 29', '21 9 15 19 39', '91 9 75 19 89', '81 99 55 59 89']
    index = 0
    T = int(input_lines[index])
    index += 1

    for _ in range(T):
        N = int(input_lines[index])
        index += 1
        gpa = list(map(float, input_lines[index].split()))
        index += 1
        tests = []
        for _ in range(5):
            scores = list(map(float, input_lines[index].split()))
            index += 1
            tests.append(scores)
        print(find_best_test(gpa, tests))

if __name__ == "__main__":
    main()
