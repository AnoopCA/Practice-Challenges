import sys
import json
import re
import numpy as np

#text = sys.stdin.read().split('\n')
with open('training.json', 'r', encoding='UTF-8') as f:
    text = f.readlines()
n = int(text[0])
text = text[1:]

def clean_text(text):
    text = re.sub(r'\s*\[duplicate\]\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*\[closed\]\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'[\n\t]+|\s{2,}', ' ', text)
    text = re.sub(r'["\'`]', '', text)
    text = re.sub(r'\s\.\.\.', '', text)
    return text.strip()

questions = []
excerpts = []
topics = []
for line in text:
    if line.strip():
        data = json.loads(line)
        topics.append(data.get('topic', ''))
        questions.append(data.get('question', '').strip())
        excerpts.append(data.get('excerpt', '').strip())

questions = [clean_text(i) for i in questions]
excerpts = [clean_text(i) for i in excerpts]

for i in range(100):
    rand = np.random.randint(0,n-1)
    print(f'{questions[rand]} -:-:- {excerpts[rand]} -:-:- {topics[rand]}')
