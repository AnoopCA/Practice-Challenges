import sys
import numpy as np
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

def clean_text(text):
    text = re.sub(r'&[^ ]*?;', ' ', text)
    text = re.sub(r'[^A-Za-z\s]', ' ', text)
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def preprocess(text):
    cities, sections, headings, categories = [], [], [], []
    for line in text:
        if line.strip():
            rows = json.loads(line)
            cities.append(rows.get('city', '').replace('.en','').strip())
            sections.append(rows.get('section', '').strip())
            headings.append(clean_text(rows.get('heading', '').lower()))
            categories.append(rows.get('category', '').strip())
    combined_text = [f'{s} {c} {h}' for c,s,h in zip(cities,sections,headings)]
    if all(x=='' for x in categories):
        return combined_text
    else:
        return combined_text, categories

def train():
    with open('training.json', 'r') as f:
        data = f.readlines()
    data = data[1:]
    combined_text, categories = preprocess(data)
    label_dict = {value:key for key,value in enumerate(set(categories))}
    labels = [label_dict[category] for category in categories]
    lr_svc_model = Pipeline([('vec', TfidfVectorizer()), ('svc', LinearSVC())])
    gb_model = Pipeline([('vec', TfidfVectorizer()), ('clf',GradientBoostingClassifier(n_estimators=250,learning_rate=0.1,max_depth=3,subsample=0.8,min_samples_split=2,min_samples_leaf=1))])
    X_train,X_test,y_train,y_test = train_test_split(combined_text, labels, test_size=0.1)
    lr_svc_model.fit(X_train, y_train)
    gb_model.fit(X_train, y_train)
    lr_svc_pred = lr_svc_model.predict(X_test)
    gb_pred = gb_model.predict(X_test)
    print(f'lr svc F1 score: {f1_score(y_test, lr_svc_pred, average="weighted")}')
    print(f'gb F1 score: {f1_score(y_test, gb_pred, average="weighted")}')
    #return lr_svc_model, label_dict

if __name__ == "__main__":
    #in_data = sys.stdin.read().strip().split('\n')
    #combined_text = preprocess(in_data[1:])
    #for i in range(25):
    train()
    #nb_model, label_dict = train()
    #pred = nb_model.predict(combined_text)
    #label_dict = {key:value for value,key in label_dict.items()}

    #for cat in pred:
    #    print(label_dict[cat])
