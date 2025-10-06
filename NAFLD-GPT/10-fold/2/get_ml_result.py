import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

train_df = pd.read_csv('./train.csv', header=None)
test_df = pd.read_csv('./test.csv', header=None)

print("train_df:", train_df.shape)
print("test_df:", test_df.shape)

X_train = train_df.iloc[:, 1:17] 
Y_train = train_df.iloc[:, 17]
X_train = X_train.astype(float)
Y_train = Y_train.astype(int)
print("X_train:", X_train.shape)
print("Y_train:", Y_train.shape)


X_test = test_df.iloc[:, 1:17]
Y_test = test_df.iloc[:, 17]
X_test = X_test.astype(float)
Y_test = Y_test.astype(int)
print("X_train:", X_test.shape)
print("Y_train:", Y_test.shape)

classifier = LogisticRegression()
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)
gt_result = Y_test
prediction_result = y_pred
print(len(prediction_result))
with open("./01-result/LR-result.txt", "w") as fout:
    print(*prediction_result, sep=",", file=fout)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)
gt_result = Y_test
prediction_result = y_pred
print(len(prediction_result))
with open("./01-result/DT-result.txt", "w") as fout:
    print(*prediction_result, sep=",", file=fout)

classifier = SVC()
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)
gt_result = Y_test
prediction_result = y_pred
print(len(prediction_result))
with open("./01-result/SVC-result.txt", "w") as fout:
    print(*prediction_result, sep=",", file=fout)

classifier = RandomForestClassifier(max_depth=4, max_features=1, random_state=0)
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)
gt_result = Y_test
prediction_result = y_pred
print(len(prediction_result))
with open("./01-result/RF-result.txt", "w") as fout:
    print(*prediction_result, sep=",", file=fout)

