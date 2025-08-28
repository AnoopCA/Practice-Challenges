import re
import sys

words = []
with open('corpus.txt', 'r') as f:
    for line in f:
        if line == "END-OF-CORPUS":
            break
        tokens = re.findall(r"[A-Za-z'-]+", line.lower())
        words.extend(tokens)
        
unq_wds = list(set(words))

def jaccard_sim(wrd):
    sim = (&) / (|)

data = sys.stdin.read().strip().split('\n')

for i in data:
    print(i)
