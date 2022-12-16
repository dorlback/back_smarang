from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
import joblib
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('write.csv', encoding = 'cp949')

f_names = ['age', 'career', 'plat','region','parti']

t_name = ['등급']

X = data[f_names]

y = data[t_name]

x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

model = RandomForestClassifier(max_depth = 80,
                               max_features = 1,
                               min_samples_leaf = 1,
                               min_samples_split = 3,
                               n_estimators = 500)

model.fit(x_train, y_train)

joblib.dump(model, 'Market.pkl') 

score = model.score(x_test, y_test)

print('학습 정확도 : '+ str(int(score*100))+' %')

y_pred = model.predict(x_test)

print('검증 정확도 : '+ str(int(accuracy_score(y_test, y_pred)*100))+' %')

print(classification_report(y_pred, y_test))












