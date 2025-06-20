import sys
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
import pandas as pd

def clean_text(text):
    text = re.sub(r'&[^ ]*?;', ' ', text)
    text = re.sub(r'[^A-Za-z0-9\s]', ' ', text)
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
    #combined_text = [f'{s} {c} {h}' for c,s,h in zip(cities,sections,headings)]
    if all(x=='' for x in categories):
        df = {'sections':sections, 'cities':cities, 'headings':headings}
        df = pd.DataFrame(df)
    else:
        df = {'sections':sections, 'categories':categories, 'cities':cities, 'headings':headings}
        df = pd.DataFrame(df)
    df['index'] = df.index

    df_community = df[df['sections']=='community']
    df_for_sale = df[df['sections']=='for-sale']
    df_housing = df[df['sections']=='housing']
    df_services = df[df['sections']=='services']
    df_list = [df_community, df_for_sale, df_housing, df_services]
    return df_list

def train(combined_text, labels):
    model = Pipeline([('vec', TfidfVectorizer()), ('clf', LinearSVC())])
    model.fit(combined_text, labels)
    return model

if __name__ == "__main__":
    categories = ['appliances', 'artists', 'photography', 'video-games', 'wanted-housing', 'household-services', 'cell-phones', 'temporary', 'automotive', 'real-estate', 'childcare', 'activities', 'shared', 'housing', 'therapeutic', 'general']
    label_dict = {cat: idx for idx, cat in enumerate(categories)}
    with open('training.json', 'r') as f:
        lines = f.readlines()[1:]

    df_train_list = preprocess(lines)
    model_list = []
    for i in range(len(df_train_list)):
        X_train = df_train_list[i]['cities'] + ' ' + df_train_list[i]['headings']
        y_train = [label_dict[cat] for cat in df_train_list[i]['categories']]
        model_list.append(train(X_train, y_train))

    reverse_dict = {v: k for k, v in label_dict.items()}
    in_data = sys.stdin.read().strip().split('\n')
    #with open('training.json', 'r') as f:
    #    in_data = f.readlines()
    df_test_list = preprocess(in_data[1:])
    pred_list = []
    for i in range(len(df_test_list)):
        X_test = df_test_list[i]['headings'] + ' ' + df_test_list[i]['cities']
        pred_list.append(model_list[i].predict(X_test))
    
    test_idx = pd.concat(df_test_list, axis=0, ignore_index=True)['index']
    pred = pd.concat([pd.Series(p) for p in pred_list], axis=0, ignore_index=True)
    pred = pred.iloc[test_idx]
    for p in pred:
        print(reverse_dict[p])
