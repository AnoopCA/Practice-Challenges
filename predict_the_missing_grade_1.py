import sys
import json
import pandas as pd
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import warnings
warnings.filterwarnings('ignore')

def get_data(data):
    subj_list = ['serial','English','Physics','Chemistry','Mathematics','ComputerScience','Biology','PhysicalEducation','Economics','Accountancy','BusinessStudies']
    students_dict_train = {key:[] for key in subj_list}
    for i in data[1:]:
        temp = json.loads(i)
        for key in students_dict_train:
            students_dict_train[key].append(temp.get(key, pd.NA))
    df = pd.DataFrame(students_dict_train)
    
    for i in subj_list:
        if i not in ['serial', 'Mathematics']:
            if 'Mathematics' in df.columns:
                if df['Mathematics'].notna().all():
                    per_class_average = df.groupby('Mathematics')[i].mean().astype(int)
                    df[i] = df[i].fillna(df['Mathematics'].map(per_class_average))
                else:
                    df[i] = df[i].fillna(df[i].mean().astype(int))
    return(df)

if __name__ == "__main__":
    with open('training.json', 'r') as f:
        data = f.readlines()
    df_train = get_data(data)
    X_train = df_train.drop(['serial','Mathematics'], axis=1)
    y_train = df_train['Mathematics']

    #data = sys.stdin.read().strip().split('\n')
    with open('sample-test.in.json', 'r') as f:
        data = f.readlines()
    df_test = get_data(data)
    X_test = df_test.drop(['serial','Mathematics'], axis=1)

    with open('sample-test.out.json', 'r') as f:
        y_test = [int(i.strip()) for i in f]

    lr_model = LogisticRegression(max_iter=1000)
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)
    print(f'f1 score - lr: {f1_score(y_test, lr_pred, average="weighted")}')

    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    print(f'f1 score - rf: {f1_score(y_test, rf_pred, average="weighted")}')
