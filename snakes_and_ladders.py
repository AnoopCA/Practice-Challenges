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
        if square in [key for key,value in ladder_squares.items()]:
            if (square + ladder_squares[square]) <= 100:
                square = ladder_squares[square]
        if square in [key for key,value in snake_squares.items()]:
            if (square - snake_squares[square]) > 0:
                square = snake_squares[square]
        if square == 100:
            break

    print(n)

if __name__ == "__main__":
    data = sys.stdin.read().strip().split('\n')
    t = int(data[0])
    rpt = 0
    for i in range(t):
        dies_probs = list(map(float, list(data[1+rpt].split(','))))
        ladder_squares = {}
        for i in data[3+rpt].split():
            ldr = list(map(int, i.split(',')))
            ladder_squares[ldr[0]] = ldr[1]
        snake_squares = {}
        for i in data[4+rpt].split():
            snk = list(map(int, i.split(',')))
            snake_squares[snk[0]] = snk[1]
        rpt += 4
    
        print_plays(dies_probs, ladder_squares, snake_squares)
    