from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

file_name = "filename.pkl" 

model = joblib.load(file_name) 

df1 = pd.DataFrame(
    {
        "매출액(억)":["2059"],
        "영업이익(억)":["71"],
        "신용등급_점수":["3"],
        "사원수(명)":["103"],
        "설립일(년)":["1986"]
    }
)

    {
        "매출액(억)":["2059"],
        "영업이익(억)":["71"],
        "신용등급_점수":["3"],
        "사원수(명)":["103"],
        "설립일(년)":["1986"]
    }

{                
               "age":["20"],
               "career":["5"],
                "plat":["400"],
                "region":"경기",
                "parti":"전업"
}



file_name = "filename.pkl" 

model = joblib.load(file_name)

print(model.predict([df1.loc[0]]))