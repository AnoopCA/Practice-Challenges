import sys
import random

def print_plays(dies_probs, ladder_squares, snake_squares):
    dies = list(range(1, len(dies_probs)+1))
    square = 1
    n = 0
    while square:
        dies_roll = random.choices(dies, weights=dies_probs, k=1)[0]
        n += 1
        if (square + dies_roll) <= 100:
            square += dies_roll
            while (square in ladder_squares) or (square in snake_squares):
                if square in ladder_squares:
                    square = ladder_squares[square]
                if square in snake_squares:
                    square = snake_squares[square]
            if n == 1000:
                return 0
            if square == 100:
                return n

if __name__ == "__main__":
    data = sys.stdin.read().strip().split('\n')
    t = int(data[0])
    rpt = 0
    for i in range(t):
        dies_probs = list(map(float, list(data[1+rpt].split(','))))
        ladder_squares = {}
        for j in data[3+rpt].split():
            ldr = list(map(int, j.split(',')))
            ladder_squares[ldr[0]] = ldr[1]
        snake_squares = {}
        for k in data[4+rpt].split():
            snk = list(map(int, k.split(',')))
            snake_squares[snk[0]] = snk[1]
        rpt += 4
        runs = []
        for _ in range(5000):
            runs.append(print_plays(dies_probs, ladder_squares, snake_squares))
        print(int(sum(runs)/len(runs)))
