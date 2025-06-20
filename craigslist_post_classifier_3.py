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

def preprocess_1(text):
    cities, sections, headings, categories = [], [], [], []
    for line in text:
        if line.strip():
            rows = json.loads(line)
            headings.append(clean_text(rows.get('heading', '').lower()))
    return headings

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
        model = train(X_train, y_train)
        model_list.append(model)
        #score = model.score(X_train, y_train)
        #print(f"Training score for model {i} (section: {df_train_list[i]['sections'].iloc[0]}): {score:.4f}")
    
    reverse_dict = {v: k for k, v in label_dict.items()}
    #in_data = sys.stdin.read().strip().split('\n')
    with open('craigslist_test.json', 'r', encoding='utf-8') as f:
        in_data = f.readlines()
    df_test_list = preprocess(in_data[1:])
    pred_list = []
    for i in range(len(df_test_list)):
        X_test = df_test_list[i]['headings'] + ' ' + df_test_list[i]['cities']
        pred_list.append(model_list[i].predict(X_test))
    pred = pd.concat([pd.Series(p) for p in pred_list], axis=0, ignore_index=True)

    test_idx = pd.concat([*df_test_list], axis=0, ignore_index=True)['index']
    pred.index = test_idx.values
    pred = pred.sort_index()

    #test_raw_data = preprocess_1(in_data[1:])
    #test_1 = pd.concat([*df_test_list], axis=0)
    #test_1 = test_1.set_index('index').loc[pred.index]
    #test_1 = pd.DataFrame({'raw_heading': test_raw_data, 'heading_after_modeling':test_1['headings']})
    #print(test_1)

    with open('test_pred.txt', 'w') as f:
        for p in pred:
            f.write(f'{reverse_dict[p]}\n')

    #for p in pred:
    #    print(reverse_dict[p])
