# Import required libraries
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Read input data
data = sys.stdin.read().strip().split('\n')
n,m = data[0].split()
n,m = int(n), int(m)

# Process training data: split by space
train_temp = [i.split() for i in data[1:n+1]]
# Extract labels (+1 or -1) and convert to binary (1 for +1, 0 for -1)
labels = [i[1] for i in train_temp]
labels = [1 if k=='+1' else 0 for k in labels]
train = [{int(j.split(':')[0]):float(j.split(':')[1]) for j in i[2:]} for i in train_temp]
train = pd.DataFrame(train)
train.drop([22,23], axis=1, inplace=True)

# Read number of queries (test samples)
q = int(data[n+1])
test_temp = [i.split() for i in data[n+2:]]
query = [i[0] for i in test_temp]
test = [{int(j.split(':')[0]):float(j.split(':')[1]) for j in i[1:]} for i in test_temp]
test = pd.DataFrame(test)
test.drop([22,23], axis=1, inplace=True)

# Scale training features
scaler = StandardScaler()
train_scaled = scaler.fit_transform(train)

# Initialize and train a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, max_depth=20, min_samples_split=5)
rf_model.fit(train, labels)
# Predict labels for test data
pred = rf_model.predict(test)
for i in range(len(query)):
    if pred[i] == 1:
        print(f'{query[i]} +1')
    else:
        print(f'{query[i]} -1')
