from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
import joblib
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('중소기업현황.csv', encoding = 'cp949')

mlist = ['매출액', '영업이익', '당기손익']
매출액 = []
영업이익 = []
당기손익 = []

for m in mlist:
    for i in range(0, data.shape[0]):
        split_ = data[m][i].replace(',','').split(' ')
        dic = {'조':0, '억':0, '만원':0}
        for j in split_:
            if '조' in j:
                dic['조'] = int(j.replace('조',''))
            if '억' in j:
                dic['억'] = int(j.replace('억',''))
            if '만원' in j:
                dic['만원'] = int(j.replace('만원',''))
        locals()[str(m)].append(dic['조']*10000 + dic['억'] + dic['만원']/10000)



# print(len(매출액), len(영업이익), len(당기손익))
data['매출액(억)'] = 매출액
data['영업이익(억)'] = 영업이익
data['당기손익(억)'] = 당기손익

employees = []
for i in range(0, data.shape[0]):
    employees.append(data['사원수'][i].split('명')[0].strip().replace(',',''))

# print(len(employees))
data['사원수(명)'] = employees


#설립연도
establish_year = []

for i in range(0, data.shape[0]):
    establish_year.append(int(data['설립일'][i].split('년')[0].strip()))
    
# print(len(establish_year))
data['설립일(년)'] = establish_year


print(data)
# [매출액(억), 영업이익(억), 신용등급_점수, 사원수(명), 설립연도(년)] 를 이용하여 등급 분류
f_names = ['매출액(억)', '영업이익(억)', '신용등급_점수', '사원수(명)', '설립일(년)']
t_name = ['등급']

X = data[f_names]
y = data[t_name]

x_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

# print(x_train.loc[0])



# model = RandomForestClassifier(max_depth = 80,
#                                max_features = 1,
#                                min_samples_leaf = 1,
#                                min_samples_split = 3,
#                                n_estimators = 500)

df1 = pd.DataFrame(
    {
        '매출액(억)':['2059'],
        '영업이익(억)':['71'],
        '신용등급_점수':['3'],
        '사원수(명)':['103'],
        '설립일(년)':['1986']
    }
)

print(df1.loc[0])


file_name = 'filename.pkl' 
model = joblib.load(file_name)

# model.fit(x_train, y_train)

print(model.predict([df1.loc[0]]))

# 학습시킨 모델을 이용하여 test데이터셋으로 학습정확도를 확인합니다.

joblib.dump(model, 'filename.pkl') 

file_name = 'filename.pkl' 

model = joblib.load(file_name) 

score = model.score(x_test, y_test)

print('학습 정확도 : '+ str(int(score*100))+' %')

y_pred = model.predict(x_test)

print('검증 정확도 : '+ str(int(accuracy_score(y_test, y_pred)*100))+' %')

print(classification_report(y_pred, y_test))

