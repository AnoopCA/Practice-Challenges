import re
import sys
import difflib

words = []
#with open('corpus.txt', 'r') as f:
with open('basic_spell_checker_data.txt', 'r') as f:
    for line in f:
        if line.strip() == "END-OF-CORPUS":
            break
        tokens = re.findall(r"[A-Za-z'-]+", line.lower())
        words.extend(tokens)
        
vocab = list(set(words))

data = sys.stdin.read().strip().split('\n')

for word in data:
    match = difflib.get_close_matches(word, vocab, n=1, cutoff=0.0)
    match = ''
    if match:
        print(f"matching text: {match[0]}")
    else:
        print(word)
