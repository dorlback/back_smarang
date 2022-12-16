from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
import joblib
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

file_name = 'Market.pkl' 

model = joblib.load(file_name) 

df1 = pd.DataFrame(
    {
        'age':['40'],
        'career':['20'],
        'plat':['10000'],
        'region':['10'],
        'parti':['4']
    }
)

print(model.predict([df1.loc[0]]))