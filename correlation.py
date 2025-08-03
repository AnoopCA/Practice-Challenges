import sys

# Read input from stdin, split into lines, and extract the number of students
data = sys.stdin.read().strip().split('\n')

n = int(data[0])

# Extract individual scores for each student and store them in a list
scores = []
for i in range(1, n+1):
    scores.append(list(map(int, data[i].split())))

# Separate the scores for Math, Physics, and Chemistry
math_scores = [i[0] for i in scores]
physics_scores = [i[1] for i in scores]
chemistry_scores = [i[2] for i in scores]

# --- Pearson Correlation: Math vs Physics ---
numerator_mp = (n * sum((math_scores[i] * physics_scores[i] for i in range(n)))) - (sum(math_scores) * sum(physics_scores))
denominator_mp = ((n*(sum(i**2 for i in math_scores))) - (sum(math_scores))**2)**0.5 * (n*sum(i**2 for i in physics_scores) - (sum(physics_scores))**2)**0.5
print(round(numerator_mp / denominator_mp, 2))

# --- Pearson Correlation: Physics vs Chemistry ---
numerator_pc = (n * sum((physics_scores[i] * chemistry_scores[i] for i in range(n)))) - (sum(physics_scores) * sum(chemistry_scores))
denominator_pc = ((n*(sum(i**2 for i in physics_scores))) - (sum(physics_scores))**2)**0.5 * (n*sum(i**2 for i in chemistry_scores) - (sum(chemistry_scores))**2)**0.5
print(round(numerator_pc / denominator_pc, 2))

# --- Pearson Correlation: Math vs Chemistry ---
numerator_mc = (n * sum((math_scores[i] * chemistry_scores[i] for i in range(n)))) - (sum(math_scores) * sum(chemistry_scores))
denominator_mc = ((n*(sum(i**2 for i in math_scores))) - (sum(math_scores))**2)**0.5 * (n*sum(i**2 for i in chemistry_scores) - (sum(chemistry_scores))**2)**0.5
print(round(numerator_mc / denominator_mc, 2))
