import sys
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
import pandas as pd

# Removes HTML entities, non-alphanumeric characters, and extra spaces
def clean_text(text):
    text = re.sub(r'&[^ ]*?;', ' ', text)
    text = re.sub(r'[^A-Za-z0-9\s]', ' ', text)
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

# Extracts and cleans 'city', 'section', 'heading', and 'category' fields. Combines them into a single text feature per entry
def preprocess(text):
    cities, sections, headings, categories = [], [], [], []
    for line in text:
        if line.strip():
            rows = json.loads(line)
            cities.append(rows.get('city', '').replace('.en','').strip())
            sections.append(rows.get('section', '').strip())
            headings.append(clean_text(rows.get('heading', '').lower()))
            categories.append(rows.get('category', '').strip())
    check_data = {'cities':cities, 'sections':sections, 'categories':categories}
    check_data = pd.DataFrame(check_data)
    print(check_data)
    combined_text = [f'{s} {c} {h}' for c,s,h in zip(cities,sections,headings)]
    if all(x=='' for x in categories):
        return combined_text
    else:
        return combined_text, categories

# Builds a pipeline with TF-IDF vectorization and Linear SVM classifier
def train(combined_text, labels):
    model = Pipeline([('vec', TfidfVectorizer()), ('clf', LinearSVC())])
    model.fit(combined_text, labels)
    return model

# Loads data, preprocesses it, trains the model, then reads test input from stdin and predicts categories
if __name__ == "__main__":
    with open('training.json', 'r') as f:
        lines = f.readlines()[1:]
    categories = ['appliances', 'artists', 'photography', 'video-games', 'wanted-housing', 'household-services', 'cell-phones', 'temporary', 'automotive', 'real-estate', 'childcare', 'activities', 'shared', 'housing', 'therapeutic', 'general']
    combined_text, labels_raw = preprocess(lines)
    label_dict = {cat: idx for idx, cat in enumerate(categories)}
    labels = [label_dict[cat] for cat in labels_raw]
    model = train(combined_text, labels)

    in_data = sys.stdin.read().strip().split('\n')
    combined_text = preprocess(in_data[1:])
    reverse_dict = {v: k for k, v in label_dict.items()}
    predictions = model.predict(combined_text)
    for pred in predictions:
        print(reverse_dict[pred])
