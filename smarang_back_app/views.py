from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Test,Marketer,Brand
import pandas as pd
from django.conf import settings
import os
from pathlib import Path
import random as ran
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')
import joblib
from rest_framework.generics import get_object_or_404 
# Create your views here.



class Modules():


    def Region_point(region):
            if region =='서울':
                return(14)  
            if region =='전체':
                return(20)  
            elif region == '경기':
                return(14)  
            else:
                return(6)  


    def Parti_pont(parti):
        if parti == '부업':
            return(4*1.5)      
        elif parti == '전업':
            return(8*1.5)

    def M_Key_get(grade):

        A_list = ['도매', '운송업', '가공', '건설업', '금속']
        B_list = ['서비스업', '도매', '통신', '플라스틱', '육류']
        C_list = ['제품', '개발', '건물', '도매', '화물']
        D_list = ['가공', '건물', '운송업', '건설업', '기계']

        if grade == ['A등급']:
            return A_list
        if grade == ['B등급']:
            return B_list
        if grade == ['C등급']:
            return C_list
        if grade == ['D등급']:
            return D_list

    def B_Key_get(grade):

        A_list = ['서비스업', '소프트웨어', '가공', '자동차', '화물','운송','기타']
        B_list = ['제품', '금속', '전기', '자동차', '가공','통신','화물']
        C_list = ['도매', '기계', '건설', '플라스틱', '전기','통신','육류']
        D_list = ['제조업', '개발', '건물', '플라스틱', '기계','육류','의료']

        if grade == ['A등급']:
            return A_list
        if grade == ['B등급']:
            return B_list
        if grade == ['C등급']:
            return C_list
        if grade == ['D등급']:
            return D_list

    

    def M_get_B(ket_list,region,job):



        brand_list = Brand.objects.filter(brand_addr__contains= region)
    
        val5_list = []

        ket_list = job+ket_list


        value=len(ket_list)
        for key_words in ket_list:
            
            
            for x in brand_list:
                if key_words in x.brand_industry:

                    val5_list.append(
                        {
                            'id':x.id,
                            'value':value,
                            'needs':x.brand_Needs
                        }
                    )

            value=value-1

        listc = []
        listd = []

        list_needs = []

        liste = []
        b_list =[]
        for x in val5_list:


            listc.append(x['id'])
            listd.append(x['value'])
            list_needs.append(x['needs'])

        count = 0
        overlap= 0
        for x in listc:
            if x not in liste:
                liste.append(x)
                b_list.append({
                    'id':listc[count],
                    'value':listd[count],
                    'needs':list_needs[count]
                })
            elif x in liste:
                overlap=overlap+1
                
                for x in b_list:

                    if x['id']==listc[count]:
                        x['value'] = x['value']+listd[count]


            count = count+1

        
    
        branlist= []

        b_list = sorted(b_list, key=(lambda x: x['value']),reverse=True)

        for x in  b_list:
            if x['value'] == b_list[0]['value']:
                branlist.append(x)
        
        branlist = sorted(branlist, key=(lambda x: x['needs']),reverse=True)

        return(branlist[0:10])


    def B_get_M(key_list,addr,industry):
   

        Marketer_list = Marketer.objects.filter(marketer_addr__contains=addr)
        
 
        del key_list[-1*len(industry):-1]
   
        key_list=industry+key_list
        val_list = []
        
        value=len(key_list)
        for key_words in key_list:

            for x in Marketer_list:
                if key_words in x.marketer_job:
                    val_list.append(
                        {
                            'id':x.id,
                            'value':value,
                            'pow':x.marketer_pow
                        }
                    )
            value=value-1

        list_id = []
        list_value = []

        list_pow = []

        list_match = []
        m_list =[]

        for x in val_list:

            list_id.append(x['id'])
            list_value.append(x['value'])
            list_pow.append(x['pow'])


        count = 0
        overlap= 0

        for x in list_id:
            if x not in list_match:
                list_match.append(x)
                m_list.append({
                    'id':list_id[count],
                    'value':list_value[count],
                    'pow':list_pow[count]                
                })
            elif x in list_match:
                overlap = overlap+1

                for x in m_list:
                    if x['id']==list_id[count]:
                        x['value'] = x['value']+list_value[count]
            
            count = count+1

        marketer= []

        m_list = sorted(m_list, key=(lambda x: x['value']),reverse=True)

        for x in m_list:
            if x['value'] == m_list[0]['value']:
                marketer.append(x)
        
        marketer = sorted(marketer, key=(lambda x: x['pow']),reverse=True)
        
        return(marketer[0:10])



        


    def Get_brandlist(brand):
        
        brand_list = []

        for x in brand:
            brand_data = get_object_or_404(Brand, pk=x['id'])
            brand_list.append(brand_data)

        return(brand_list)

    def Get_marketerlist(marketer):
        
        marketer_list = []

        for x in marketer:
            marketer_data = get_object_or_404(Marketer, pk=x['id'])
            marketer_list.append(marketer_data)

        return(marketer_list)

        


class Ai_test(APIView):

    def post(self,request):

        
        base_dir =settings.BASE_DIR
        ai_model = os.path.join(base_dir,Path('smarang_back_app\Ai_data\Brand\Filename.pkl'))
        model = joblib.load(ai_model) 

        industry = request.data['industry']
        addr = request.data['addr']
        req_dict = request.data
        del(req_dict['industry'])
        del(req_dict['addr'])
        
        df1 = pd.DataFrame(req_dict)

        print(model.predict([df1.loc[0]]))

        key_list = Modules.B_Key_get(model.predict([df1.loc[0]]))

        marketer = Modules.B_get_M(key_list,addr,industry)

        marketer_list = Modules.Get_marketerlist(marketer)
        
        return_list = []

        for x in marketer_list:
            return_list.append({'마케터 나이':x.marketer_age,'주소':x.marketer_addr,'경력':x.marketer_job,'경력 년수':x.marketer_career,'참여형식':x.marketer_form})
        return Response( status=status.HTTP_201_CREATED)


class Brand_getMarketer(APIView):

    def post(self,request):

        base_dir =settings.BASE_DIR
        ai_model = os.path.join(base_dir,Path('smarang_back_app/Ai_data/Brand/Filename.pkl'))
        model = joblib.load(ai_model) 

        industry = request.data['industry']
        addr = request.data['addr']
        req_dict = request.data
        del(req_dict['industry'])
        del(req_dict['addr'])
        
        df1 = pd.DataFrame(req_dict)


        key_list = Modules.B_Key_get(model.predict([df1.loc[0]]))

        marketer = Modules.B_get_M(key_list,addr,industry)

        marketer_list = Modules.Get_marketerlist(marketer)
        
        return_list = []

        for x in marketer_list:
            return_list.append({'마케터_나이':x.marketer_age,'주소':x.marketer_addr,'경력':x.marketer_job,'경력_년수':x.marketer_career,'참여형식':x.marketer_form})

        return Response( return_list,status=status.HTTP_201_CREATED)

class Marketer_getBrand(APIView):

    def post(self,request):

        
        
        base_dir =settings.BASE_DIR
        ai_model = os.path.join(base_dir,Path('smarang_back_app/Ai_data/Marketer/Market.pkl'))
        model = joblib.load(ai_model) 

        region = request.data['region']
        request.data['region'] = Modules.Region_point(request.data['region'])
        request.data['parti'] = Modules.Parti_pont(request.data['parti'])
        
        job =  request.data['job']      

        print(job)

        req_dict = request.data
        del(req_dict['job'])
        
        df1 = pd.DataFrame(req_dict)
        
        key_list = Modules.M_Key_get(model.predict([df1.loc[0]]))

        brand = Modules.M_get_B(key_list,region,job)
        brand_list = Modules.Get_brandlist(brand)


        print(brand_list)
        return_list = []
                
        for x in brand_list:
            return_list.append({'기업이름':x.brand_name,'주소':x.brand_addr,'상세업종':x.brand_industry})

        return Response(return_list, status=status.HTTP_201_CREATED)

class Brand_getgrade(APIView):

    def post(self,request):
        
        base_dir =settings.BASE_DIR
        ai_model = os.path.join(base_dir,Path('smarang_back_app\Ai_data\Brand\Filename.pkl'))
        model = joblib.load(ai_model) 

        df1 = pd.DataFrame(request.data)

        print(model.predict([df1.loc[0]]))

        return Response( status=status.HTTP_201_CREATED)



class Marketer_getgrade(APIView):

    def post(self,request):

        base_dir =settings.BASE_DIR
        ai_model = os.path.join(base_dir,Path('smarang_back_app\Ai_data\Marketer\Market.pkl'))
        model = joblib.load(ai_model) 


        request.data['region'] = Modules.Region_point(request.data['region'])
        request.data['parti'] = Modules.Parti_pont(request.data['parti'])

        df1 = pd.DataFrame(request.data)

        print(model.predict([df1.loc[0]]))


        return Response( status=status.HTTP_201_CREATED)