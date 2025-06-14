import sys
import json
import re
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def clean_text(text):
    text = re.sub(r'\s*\[duplicate\]\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s*\[closed\]\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'[\n\t]+|\s{2,}', ' ', text)
    text = re.sub(r'["\'`]', '', text)
    text = re.sub(r'\s\.\.\.', '', text)
    return text.strip()

def get_data(text):
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
    train = [questions[i]+ '[SEP]' + excerpts[i] for i in range(len(questions))]
    if all(x=='' for x in topics):
        return train
    else:
        return train, topics

def train():
    with open('training.json', 'r', encoding='UTF-8') as f:
        text = f.readlines()
    text = text[1:]
    train, topics = get_data(text)
    label_dict = {value:num for num,value in enumerate(set(topics))}
    labels = [label_dict[i] for i in topics]
    pipeline = Pipeline([('vect', CountVectorizer()), ('nb', MultinomialNB())])
    pipeline.fit(train, labels)
    return pipeline, label_dict

if __name__ == "__main__":
    text_in = sys.stdin.read().split('\n')
    text_in = text_in[1:]
    test = get_data(text_in)
    model, label_dict = train()
    pred = model.predict(test)
    label_dict = {v:k for k,v in label_dict.items()}
    for i in pred:
        print(label_dict[i])
