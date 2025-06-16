import sys
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, log_loss, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB

data = sys.stdin.read().strip().split('\n')
n,m = data[0].split()
n,m = int(n), int(m)

train_temp = [i.split() for i in data[1:n+1]]
labels = [i[1] for i in train_temp]
labels = [1 if k=='+1' else 0 for k in labels]
train = [{int(j.split(':')[0]):float(j.split(':')[1]) for j in i[2:]} for i in train_temp]
train = pd.DataFrame(train)
train.drop([22,23], axis=1, inplace=True)

q = int(data[n+1])
test_temp = [i.split() for i in data[n+2:]]
query = [i[0] for i in test_temp]
test = [{int(j.split(':')[0]):float(j.split(':')[1]) for j in i[1:]} for i in test_temp]
test = pd.DataFrame(test)
test.drop([22,23], axis=1, inplace=True)

scaler = StandardScaler()
train_scaled = scaler.fit_transform(train)

X_train,X_test,y_train,y_test = train_test_split(train_scaled,labels,test_size=0.2)

rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
pred = rf_model.predict(X_test)
print('RandomForest Classifier:')
print(confusion_matrix(y_test, pred))
print('log loss: ', log_loss(y_test, pred))
print('f1_score: ', f1_score(y_test, pred))
print('accuracy: ', accuracy_score(y_test, pred))

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
pred = lr_model.predict(X_test)
print('Logistic Regression:')
print(confusion_matrix(y_test, pred))
print('log loss: ', log_loss(y_test, pred))
print('f1_score: ', f1_score(y_test, pred))
print('accuracy: ', accuracy_score(y_test, pred))

svc_model = SVC()
svc_model.fit(X_train, y_train)
pred = svc_model.predict(X_test)
print('SVM Classifier:')
print(confusion_matrix(y_test, pred))
print('log loss: ', log_loss(y_test, pred))
print('f1_score: ', f1_score(y_test, pred))
print('accuracy: ', accuracy_score(y_test, pred))

nb_model = BernoulliNB()
nb_model.fit(X_train, y_train)
pred = nb_model.predict(X_test)
print('Naive Bayes:')
print(confusion_matrix(y_test, pred))
print('log loss: ', log_loss(y_test, pred))
print('f1_score: ', f1_score(y_test, pred))
print('accuracy: ', accuracy_score(y_test, pred))
