import sys
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

def clean_text(text):
    #text = re.sub(r'[^A-Za-z0-9\s]', '', text)
    return text

def preprocess(text):
    cities = []
    sections = []
    headings = []
    categories = []
    for line in text:
        if line.strip():
            rows = json.loads(line)
            cities.append(rows.get('city', '').strip())
            sections.append(rows.get('section', '').strip())
            headings.append(rows.get('heading', '').strip())
            categories.append(rows.get('category', '').strip())
    headings = [clean_text(i) for i in headings]
    combined_text = [f'{city} {section} {heading}' for city,section,heading in zip(cities,sections,headings)]
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
    rf_model = Pipeline([('vec', TfidfVectorizer()), ('rf', RandomForestClassifier())])
    lr_model = Pipeline([('vec', TfidfVectorizer()), ('lr', LogisticRegression())])
    nb_model = Pipeline([('vec', TfidfVectorizer()), ('nb', MultinomialNB())])
    X_train,X_test,y_train,y_test = train_test_split(combined_text, labels, test_size=0.1)
    rf_model.fit(X_train, y_train)
    lr_model.fit(X_train, y_train)
    nb_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    lr_pred = lr_model.predict(X_test)
    nb_pred = nb_model.predict(X_test)
    print(f'rf f1score: {f1_score(y_test, rf_pred)}')
    print(f'lr f1score: {f1_score(y_test, lr_pred)}')
    print(f'nb f1score: {f1_score(y_test, nb_pred)}')
    return nb_model, label_dict

if __name__ == "__main__":
    in_data = sys.stdin.read().strip().split('\n')
    combined_text = preprocess(in_data[1:])
    nb_model, label_dict = train()
    pred = nb_model.predict(combined_text)
    label_dict = {key:value for value,key in label_dict.items()}

    for cat in pred:
        print(label_dict[cat])
