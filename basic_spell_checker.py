import re
import sys
from collections import Counter
import math

words = []
#with open('corpus.txt', 'r') as f:
with open('basic_spell_checker_data.txt', 'r') as f:
    for line in f:
        if line == "END-OF-CORPUS":
            break
        tokens = re.findall(r"[A-Za-z'-]+", line.lower())
        words.extend(tokens)
        
vocab = list(set(words))

def cosine_sim(wd1, wd2):
    vec1, vec2 = Counter(wd1), Counter(wd2)
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum(vec1[i] * vec2[i] for i in intersection)
    denominator = math.sqrt(sum(v**2 for v in vec1.values())) * math.sqrt(sum(v**2 for v in vec2.values()))
    return numerator / denominator if denominator else 0.0

#data = sys.stdin.read().strip().split('\n')

data = ['bberant', 'bberation', 'bbrieviated', 'bbriviated', 'bbriviation', 'bcess', 'beration', 'berrent', 'bilites', 'billity', 'bilty', 'bit of',
        'bnormalites', 'bondon', 'bortificant', 'breviate', 'breviation', 'britrary', 'bscence' 'bsense', 'bsorbancy', 'bsorbant', 'bsorbsion', 'bsorbtion']

wd_score = 0
match_text = ''
for in_txt in data:
    for wd_vocab in vocab:
        score = cosine_sim(in_txt, wd_vocab)
        if score > wd_score:
            wd_score = score
            match_text = wd_vocab
    if match_text:
        print(match_text)
    else:
        print(in_txt)
