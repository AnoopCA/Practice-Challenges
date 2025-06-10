import sys
import numpy as np
from scipy.sparse import hstack, csr_matrix
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.model_selection import GridSearchCV
#from sklearn.model_selection import train_test_split

train = pd.read_csv('trainingdata.txt', header=None, names=['text'])
train = train.iloc[1:].reset_index(drop=True)

train['labels'] = train['text'].apply(lambda x: int(x[0]))
train['text'] = train['text'].apply(lambda x: x[1:].strip())
train['text'] = train['text'].apply(lambda x: str.lower(x))
train['text_len'] = train['text'].apply(lambda x: len(x))

max_size = train['labels'].value_counts().max()
lst = [train]
for class_index, group in train.groupby('labels'):
    lst.append(group.sample(max_size - len(group), replace=True))
df_balanced = pd.concat(lst)
text = df_balanced['text']
text_len = df_balanced['text_len']
y_train = df_balanced['labels']

bow_model = CountVectorizer()
bow_train = bow_model.fit_transform(text)
tfidf_model = TfidfVectorizer()
tfidf_train = tfidf_model.fit_transform(text)
text_len = csr_matrix(text_len.values.reshape(-1,1))
bow_tfidf_train = hstack((bow_train, tfidf_train, text_len)).tocsr()

#X_train,X_test,y_train,y_test = train_test_split(bow_tfidf_train, y_train, stratify=y_train, test_size=0.2)
#nb_model = MultinomialNB()
#params = {'alpha':[0.05, 0.01, 0.1, 0.5]}
#search = GridSearchCV(estimator=nb_model, param_grid=params, scoring='accuracy', cv=3, #return_train_score=True)
#search_out = search.fit(X_train,y_train)
#param_values = params.get('alpha')
#Train_scores = search_out.cv_results_['mean_train_score']
#CV_scores = search_out.cv_results_['mean_test_score']
#print(param_values)
#print(CV_scores)

X_train = bow_tfidf_train
nb_model = MultinomialNB(alpha=0.01)
nb_model.fit(X_train, y_train)
test_in = sys.stdin.read().strip().split('\n')
test_in = [i.lower() for i in test_in]
bow_test = bow_model.transform(test_in[1:])
tfidf_test = tfidf_model.transform(test_in[1:])
test_text_len = np.array([len(test_in[i]) for i in range(1,len(test_in))])
test_text_len = csr_matrix(test_text_len.reshape(-1,1))
bow_tfidf_test = hstack((bow_test, tfidf_test, test_text_len)).tocsr()
x_test = bow_tfidf_test
y_pred = nb_model.predict(x_test)
for i in y_pred:
    print(i)
