import pandas as pd
from konlpy.tag import Okt
from collections import Counter
import operator
okt = Okt()



def make_noun(str_data):
    # noun = okt.nouns(dataA[0].상세업종)
    noun = okt.nouns(str_data)

    for b in noun:
            if len(b)<2:
                noun.remove(b)
            if '기타' in noun:    
                noun.remove('기타')

    for b in noun:
            if len(b)<2:
                noun.remove(b)
            if '기타' in noun:    
                noun.remove('기타')
            elif '일반' in noun:    
                noun.remove('일반')
            elif '관련' in noun:    
                noun.remove('관련')
            elif '부품' in noun:    
                noun.remove('부품')
            elif '기기' in noun:    
                noun.remove('기기')
            elif '장비' in noun:    
                noun.remove('장비')
            elif '처리' in noun:    
                noun.remove('처리')
            elif '종합' in noun:    
                noun.remove('종합')           
            elif '자재' in noun:    
                noun.remove('자재')  
            elif '대리' in noun:    
                noun.remove('대리')
            elif '상품' in noun:    
                noun.remove('상품') 
            elif '사업' in noun:    
                noun.remove('사업')  
    return(noun)



def Get_sector(list_data):
    counter = Counter(sum(list_data, []))



    d1 = sorted(dict(counter).items(), key=operator.itemgetter(1), reverse=True)

    Secotrs = []

    for x in range(6):
        Secotrs.append(list(dict(d1).keys())[x])

    print()
    return(Secotrs)


data = pd.read_csv('write.csv', encoding = 'cp949')

mlist = ['직업경력','등급']

data_after = data[mlist]

dataA = []
dataB = []
dataC = []
dataD = []


for column_name, rows  in data[mlist].iterrows():

    if rows.등급 == 'A등급':
        
        dataA.append(
            make_noun(rows.직업경력)
        )

    elif rows.등급 == 'B등급':
        dataB.append(
            make_noun(rows.직업경력)
        )
    elif rows.등급 == 'C등급':
        dataC.append(
            make_noun(rows.직업경력)
        )
    elif rows.등급 == 'D등급':
        dataD.append(
            make_noun(rows.직업경력)
        )


A_Sectors = Get_sector(dataA)
B_Sectors = Get_sector(dataB)
C_Sectors = Get_sector(dataC)
D_Sectors = Get_sector(dataD)


print('A등급 업종 :')
print(A_Sectors)
print('B등급 업종 :')
print(B_Sectors)
print('C등급 업종 :')
print(C_Sectors)
print('D등급 업종 :')
print(D_Sectors)

