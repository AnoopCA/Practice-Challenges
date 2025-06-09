import sys
from scipy.sparse import hstack
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize
import string
import re
import spacy

# Download English word list and tokenizer
nltk.download('words')
nltk.download('punkt')
nltk.download('punkt_tab')

train = pd.read_csv('trainingdata.txt', header=None, names=['text'])
train = train.iloc[1:].reset_index(drop=True)

train['labels'] = train['text'].apply(lambda x: int(x[0]))
train['text'] = train['text'].apply(lambda x: x[1:].strip())
train['text'] = train['text'].apply(lambda x: str.lower(x))
english_vocab = set(w.lower() for w in words.words())
#nlp = spacy.load('en_core_web_sm')
#english_vocab = set([w.lower_ for w in nlp.vocab if w.is_alpha])
def extract_non_english(text):
    tokens = word_tokenize(text.lower())
    tokens = [re.sub(r'\W+', '', token) for token in tokens if token.isalpha()]
    non_english = [word for word in tokens if word not in english_vocab]
    return non_english
non_english = []
train['non_english'] = train['text'].apply(extract_non_english)
non_eng = train['non_english'].to_list()
unique_words = [j for i in non_eng for j in i]
unique_words = set(unique_words)
print(unique_words)
print(len(unique_words))

sys.exit()

#train['text_len'] = train['text'].str.len()

bow_model = CountVectorizer()
bow_train = bow_model.fit_transform(train['text'])
tfidf_model = TfidfVectorizer()
tfidf_train = tfidf_model.fit_transform(train['text'])
bow_tfidf_train = hstack((bow_train, tfidf_train)).tocsr()

X_train,X_test,y_train,y_test = train_test_split(bow_tfidf_train, train['labels'], stratify=train['labels'], test_size=0.2)
nb_model = MultinomialNB()
params = {'alpha':[0.05, 0.01, 0.1, 0.5]}
search = GridSearchCV(estimator=nb_model, param_grid=params, scoring='accuracy', cv=3,return_train_score=True)
search_out = search.fit(X_train,y_train)
param_values = params.get('alpha')
Train_scores = search_out.cv_results_['mean_train_score']
CV_scores = search_out.cv_results_['mean_test_score']
print(param_values)
print(CV_scores)
print(train['text'].tail())

#nb_model.fit(X_train, y_train)
#pred = nb_model.predict(X_test)
#score = accuracy_score(y_test, pred)
#print(score)

#X_train = bow_tfidf_train
#y_train = train['labels']
#nb_model = MultinomialNB()
#nb_model.fit(X_train, y_train)
#test_in = sys.stdin.read().strip().split('\n')
#bow_test = bow_model.transform(test_in[1:])
#tfidf_test = tfidf_model.transform(test_in[1:])
#bow_tfidf_test = hstack((bow_test, tfidf_test)).tocsr()
#x_test = bow_tfidf_test
#y_pred = nb_model.predict(x_test)
#for i in y_pred:
#    print(i)
