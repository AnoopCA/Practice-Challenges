from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
x_train=[] 
y_train=[]
with open('trainingdata.txt') as f: 
    l = f.readline() 
    for line in f: 
        temp = line.split() 
        n=len(temp) 
        y_train.append(int(temp[0]))
        x_train.append( " ".join(temp[1:n]) )

inp = int(input())
x_test=[]
text_clf = Pipeline([('vect', CountVectorizer()),('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, max_iter=8, random_state=42))])
text_clf = text_clf.fit(x_train,y_train)
for data in range(inp): 
    temp = str(input()) 
    x_test.append(temp)

output=text_clf.predict(x_test)
for i in range(inp): 
    print(output[i])