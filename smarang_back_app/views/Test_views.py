from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Ai_version,Brand_detail,Marketer_detail,Test,Marketer,Brand,Brand_status,Brand_dummy,Terms,User,UserManager,Marketer_user,Brand_user,Button_con,Cal_table,Button_status,Marketer_user,Cal_data,AuthSMS,Items,Item_list,Perform_data,Perform_list,Brand_raw,Item_succ
import pandas as pd
from django.conf import settings
import os
from pathlib import Path
import random as ran
import warnings
from rest_framework.generics import get_object_or_404 
from datetime import date
from random import randint
from django.contrib.auth.hashers import check_password
from django.db.models import Q

warnings.filterwarnings('ignore')


class User_create(APIView):

    def post(self,request):
        
        # User.objects.create(
        # )

        UserManager.create_user(
            self=User.objects,
            email = 'bsh7229@gmail.com',
            nickname = 'dorl',
            password = 'pass1234'
        )
        
        

        return Response( status=status.HTTP_201_CREATED)
        
        

class Marketer_create(APIView):

    def post(self,request):

        user = UserManager.create_user(
            self=User.objects,
            email= request.data['Email'],
            nickname= request.data['Email'],
            password = request.data['Password'],
            name = request.data['name']
        )

        m_user = Marketer_user.objects.create(
            user_id = user,
            phoneNumber= request.data['phone_number'].replace("-",""),
        )
        
        Marketer_detail.objects.create(
            marketer_id=m_user

        )

        return Response( status=status.HTTP_201_CREATED)   

        

class Marketer_subscribe_create(APIView):

    def post(self,request):
        
        email = request.data['email']

        user = Marketer_user.objects.get(user_id = User.objects.get(email = email))

        m_user = Marketer_detail.objects.get(marketer_id = user)



        if (m_user.marketer_age != '' and m_user.marketer_age != None) and (m_user.marketer_addr != '' and m_user.marketer_addr != None) and (m_user.marketer_job != '' and m_user.marketer_job != None) and (m_user.marketer_career != '' and m_user.marketer_career != None) and (m_user.marketer_form != '' and m_user.marketer_form != None) and (m_user.marketer_plat != '' and m_user.marketer_plat != None):

            print(m_user.marketer_age)

            applicate = Item_succ.objects.create(
                Marketer_id = Marketer_user.objects.get(user_id = User.objects.get(email = email)),
                Item_title = 'SCRM',
                Item_id_per = Items.objects.get(Item_title='SCRM')
            )

            data={'succ'}
        else:
            
            data={'no_detail'}

        return Response( data,status=status.HTTP_201_CREATED)  

                                                                                         
class Marketer_list_get(APIView):

    def post(self,request):
        email = request.data['email']

        m_user_list = Item_succ.objects.filter(Item_id_per = Items.objects.get(Brand_user_id = Brand_user.objects.get(user_id = User.objects.get(nickname = email))))
        
        data_list = []

        for x in m_user_list:
            print(x.id)
            data = {
                'email' : x.Marketer_id.user_id.email,
                'phone' : x.Marketer_id.phoneNumber,
                'name' : x.Marketer_id.user_id.name,
                'userstate' : x.userstate,
                'perform' : len(Perform_data.objects.filter(Marketer_id = x.Marketer_id)) ,
                'id': x.id
            }
            data_list.append(data)
          

        return Response(data_list, status=status.HTTP_201_CREATED)  

class Marketer_list_search_get(APIView):

    def post(self,request):
        email = request.data['email']         
        state = request.data['state']      
        name = request.data['name']      
        phone = request.data['phone']      
        email_get = request.data['email_get']      
        
        
                                              
        m_user_list = Item_succ.objects.filter(Item_id_per = Items.objects.get(Brand_user_id = Brand_user.objects.get(user_id = User.objects.get(nickname = email))))
        
        data_list = []

        

        for x in m_user_list:
                        
            

            if state in str(x.userstate) and name in str(x.Marketer_id.user_id.name) and phone in str(x.Marketer_id.phoneNumber) and email_get in str(x.Marketer_id.user_id.email):
                data = {
                'email' : x.Marketer_id.user_id.email,
                'name' : x.Marketer_id.user_id.name,
                'phone' : x.Marketer_id.phoneNumber,
                'userstate' : x.userstate,
                'perform' : len(Perform_data.objects.filter(Marketer_id = x.Marketer_id)) ,
                'id': x.id
                }
                data_list.append(data)

          

        return Response(data_list, status=status.HTTP_201_CREATED)  

class Marketer_state_change(APIView):

    def post(self,request):
        id = request.data['id']
        state = request.data['userstate']

        if(state == 'true'):
            state = True
        else:
            state =False

        item_succ = Item_succ.objects.get(pk = id)
        item_succ.userstate = state
        item_succ.save()


        return Response( status=status.HTTP_201_CREATED)  

class Marketer_Market_list(APIView):

    def post(self,request):
        
        email = request.data['email']

        data_list = Item_succ.objects.filter(Marketer_id = Marketer_user.objects.get(user_id=User.objects.get(email = email)))
        
        data_res = []



        for x in data_list:
            data_form={
                'userstate':x.userstate,
                'Item_title':x.Item_title
            }

            data_res.append(data_form)
        data={
            'list':data_res,
        }
        return Response(data, status=status.HTTP_201_CREATED)  


class Brand_create(APIView):

    def post(self,request):
        
        
        
        user = UserManager.create_user(
            self=User.objects,
            email= request.data['Email'],
            nickname= request.data['Email'],
            password = request.data['Password'],   
            name = request.data['name']
        )

        b_user = Brand_user.objects.create( 
            user_id = user,
            phoneNumber= request.data['phone_number'].replace("-",""),
            buisnessNumber = request.data['buisnessNumber']
        )
        Brand_detail.objects.create(

            brand_id = b_user,
            brand_name = request.data['brand_name'] ,
            brand_addr = request.data['brand_addr'],
            brand_date = request.data['brand_date'],
            brand_price = request.data['brand_price'],
            brand_profit = request.data['brand_profit'],
            brand_credit_grade_score = request.data['brand_credit_grade_score'],
            brand_employees = request.data['brand_employees'],
            brand_industry = request.data['brand_industry']

        )
        br = Brand_raw.objects.create(
                brand_name = request.data['brand_name'] ,
                brand_addr = request.data['brand_addr'],
                brand_date = request.data['brand_date'],
                brand_scale = '',
                brand_shape = '',
                brand_price = request.data['brand_price'],
                brand_profit = request.data['brand_profit'],
                brand_profit_loss = '',
                brand_credit_grade = '',
                brand_credit_grade_score = request.data['brand_credit_grade_score'],
                brand_employees =  request.data['brand_employees'],
                brand_industry = request.data['brand_industry'],
                brand_Needs = '',
                brand_grade = '',
        )
        bs = Brand_status.objects.create(
                brand_id = br,
        )
        Brand_dummy.objects.create(
            brand_id =bs
        )

        
        return Response( status=status.HTTP_201_CREATED) 



class Login_view(APIView):

    

    def post (self,request):

        nickname = request.data['username']
        password = request.data['password']
        res_data ={}

        try:

            if not (nickname  and password ):

                res_data['error'] = '모든 값을 입력해야 합니다!'
                
                

            else:
                user = User.objects.get(nickname=nickname)
                if check_password(password, user.password):
                    #--------------------------------------------------------------------
                
                    request.session['user'] = user.id # user key에 로그인한 user의 아이디 값
                    #변수에 값넣음
                                    
                    try:
                        user_data = Marketer_user.objects.get(user_id = user.id)
                        cate = 'marketer'
                    
                    except:
                        user_data = Brand_user.objects.get(user_id = user.id)
                        cate = 'brand'

                    if not request.session.session_key:
                        request.session.save()
                    session_id = request.session.session_key

                    

                    data={
                        'succ':True,
                        'key':session_id,
                        'email':nickname,
                        'user_id':request.session['user'],
                        'cate':cate
                    }

                    print(data)

                    return Response( data,status=status.HTTP_201_CREATED)   
                    #비밀번호 일치, 로그인 처리
                    #세션
                    #---------------------------------------------------------------------

                else:
                    data={
                        'succ':False
                    }

            return Response(data, status=status.HTTP_201_CREATED)

        except:

            data={
                        'succ':False
                }

            return Response(data, status=status.HTTP_201_CREATED)


class Item_list_get_view(APIView):    

    def post(self,request):
        try:
            item_url = request.data['url']
            item_data = Items.objects.get(Item_url = item_url)
            item_list = Item_list.objects.filter(Item_id = item_data.id)

            

            list = []

            for x in item_list:
                list.append(x.Title)

            list.insert(0, 'NO')
            list.insert(1, '대리점')
            list.insert(2, '등록일')
            list.append( '정산')
            list.append( '수정')
          
    
            
          
            perform = Perform_data.objects.filter(Item_id_per = item_data.id)
            
            perfrom_data_list = []
                
            for x in perform:
                    
                    per_list = []
            
                    per_data = Perform_list.objects.filter(Perform_id = x.id)
                    for y in per_data:
                        per_list.append({y.title:y.data})
                    per_list.insert(0,{'marketer':[x.Marketer_id.user_id.name,'']})
                    per_list.insert(1,{'created_date':x.created_at})

                    perfrom_data_data={
                        'id':x.id,
                        'list':per_list
                    }


                    
                    perfrom_data_list.append(perfrom_data_data)
                
        
            data={ 
                'title':item_data.Item_title,
                'url':item_data.Item_url,
                'created':item_data.created_at,
                'list':list,
                'item_list_data':perfrom_data_list,
            }



        except:
            list=[]
            perfrom_data_list=[]
            data={
                'title':'',
                'url':'/',
                'created':'',
                'list':list,
                'item_list_data':perfrom_data_list,
            }
        return Response( data,status=status.HTTP_201_CREATED)   

class Item_list_get_search_view(APIView):    

    def post(self,request):


        review = request.data['review']
        search = request.data['search']
        
        

        try:
            item_url = request.data['url']
            item_data = Items.objects.get(Item_url = item_url)
            item_list = Item_list.objects.filter(Item_id = item_data.id)

            

            list = []

            for x in item_list:
                list.append(x.Title)

            list.insert(0, 'NO')
            list.insert(1, '대리점')
            list.insert(2, '등록일')
            list.append( '정산')
            list.append( '수정')
          
    
            
          
            perform = Perform_data.objects.filter(Item_id_per = item_data.id)

            per_data_list2 = []
            for x in perform:
             
                    setstate= False
                    
                    per_data = Perform_list.objects.filter(Perform_id = x.id)
                    for y in per_data:

                        

                        if y.title == 'button':
                            if(review in y.data):
                                setstate=True
 

                    if(setstate==True):
                    
                     
                        per_data_list2.append(x)

            
            

                          
 
            per_data_list = []
            for x in per_data_list2:
             
                    setstate= False
                    
                    per_data = Perform_list.objects.filter(Perform_id = x.id)
                    for y in per_data:

                        

                        if search in y.data:
                            setstate=True
 

                    if(setstate==True):
                    
                     
                        per_data_list.append(x)
            
            print(per_data_list)
            perfrom_data_list = []
                
            for x in per_data_list:
                    
                    per_list = []
            
                    per_data = Perform_list.objects.filter(Perform_id = x.id)
                    for y in per_data:
                        per_list.append({y.title:y.data})
                    per_list.insert(0,{'marketer':[x.Marketer_id.user_id.name,'']})
                    per_list.insert(1,{'created_date':x.created_at})

                    perfrom_data_data={
                        'id':x.id,
                        'list':per_list
                    }


                    
                    perfrom_data_list.append(perfrom_data_data)
                
        
            data={ 
                'title':item_data.Item_title,
                'url':item_data.Item_url,
                'created':item_data.created_at,
                'list':list,
                'item_list_data':perfrom_data_list,
            }



        except:
            list=[]
            perfrom_data_list=[]
            data={
                'title':'',
                'url':'/',
                'created':'',
                'list':list,
                'item_list_data':perfrom_data_list,
            }
        return Response( data,status=status.HTTP_201_CREATED)   

class Item_list_get_view_m(APIView):    

    def post(self,request):
        
        try:
            item_url = request.data['url']
            user_email = request.data['email']
            item_data = Items.objects.get(Item_url = item_url)
            item_list = Item_list.objects.filter(Item_id = item_data.id)
            user_data = Marketer_user.objects.get(user_id = User.objects.get(email = user_email))
            item_succ = Item_succ.objects.get(Marketer_id= user_data, Item_id_per = item_data)

            

            if(item_succ.userstate==True):
                
                list = []

                for x in item_list:
                    list.append(x.Title)

                list.insert(0, 'NO')
                list.insert(1, '대리점')
                list.insert(2, '등록일')
                list.append( '정산')
                list.append( '수정')
            

                

                perform = Perform_data.objects.filter(Item_id_per = item_data.id,Marketer_id = user_data) 
                
                
                perfrom_data_list = []
                
                for x in perform:

                    
                    per_list = []
            
                    per_data = Perform_list.objects.filter(Perform_id = x.id)
                    for y in per_data:
                        per_list.append({y.title:y.data})
                    per_list.insert(0,{'marketer':[x.Marketer_id.user_id.name,'']})
                    per_list.insert(1,{'created_date':x.created_at})

                    perfrom_data_data={
                        'id':x.id,
                        'list':per_list
                    }


                    
                    perfrom_data_list.append(perfrom_data_data)
                
                data={
                   
                    'title':item_data.Item_title,
                    'url':item_data.Item_url,
                    'created':item_data.created_at,
                    'list':list,
                    'item_list_data':perfrom_data_list,

                }

                
                
                
                print(perfrom_data_list)

                return Response( data,status=status.HTTP_201_CREATED)
            else:
                return Response( status=status.HTTP_201_CREATED)

        

        except:
            list=[]
            perfrom_data_list=[]
            data={
                'title':'',
                'url':'/',
                'created':'',
                'list':list,
                'item_list_data':perfrom_data_list,

            }
        return Response( data,status=status.HTTP_201_CREATED)

class Item_perform_del(APIView):    
    def post(self,request):

        id = request.data['id']

        perform = Perform_data.objects.get(pk = id)

        perform.delete()

        return Response( status=status.HTTP_201_CREATED)

class Item_list_get_view_search_m(APIView):    

    def post(self,request):
        

        # marketer = request.data['marketer']
        review = request.data['review']
        search = request.data['search']
        

        

        try:
            item_url = request.data['url']
            user_email = request.data['email']
            item_data = Items.objects.get(Item_url = item_url)
            item_list = Item_list.objects.filter(Item_id = item_data.id)
            user_data = Marketer_user.objects.get(user_id = User.objects.get(email = user_email))
            item_succ = Item_succ.objects.get(Marketer_id= user_data, Item_id_per = item_data)

            

            if(item_succ.userstate==True):
                
                list = []

                for x in item_list:
                    list.append(x.Title)

                list.insert(0, 'NO')
                list.insert(1, '대리점')
                list.insert(2, '등록일')
                list.append( '정산')
                list.append( '수정')
            

                

                perform = Perform_data.objects.filter(Item_id_per = item_data.id,Marketer_id = user_data ) 

                per_data_list2 = []
                for x in perform:
             
                    setstate= False
                    
                    per_data = Perform_list.objects.filter(Perform_id = x.id)
                    for y in per_data:

                        

                        if y.title == 'button':
                            if(review in y.data):
                                setstate=True
 

                    if(setstate==True):
                    
                     
                        per_data_list2.append(x)

                          
 
                per_data_list = []
                for x in per_data_list2:
             
                    setstate= False
                    
                    per_data = Perform_list.objects.filter(Perform_id = x.id)
                    for y in per_data:

                        

                        if search in y.data:
                            setstate=True
 

                    if(setstate==True):
                    
                     
                        per_data_list.append(x)
                        



                perfrom_data_list = []
                
                for x in per_data_list:

                    
                    per_list = []
            
                    per_data = Perform_list.objects.filter(Perform_id = x.id)

                    
                    for y in per_data:
                        per_list.append({y.title:y.data})

                    per_list.insert(0,{'marketer':[x.Marketer_id.user_id.name,'']})
                    per_list.insert(1,{'created_date':x.created_at})


                    perfrom_data_data={
                        'id':x.id,
                        'list':per_list
                    }



                    perfrom_data_list.append(perfrom_data_data)
                
                data={
                   
                    'title':item_data.Item_title,
                    'url':item_data.Item_url,
                    'created':item_data.created_at,
                    'list':list,
                    'item_list_data':perfrom_data_list,

                }

     

                return Response( data,status=status.HTTP_201_CREATED)
            else:
                return Response( status=status.HTTP_201_CREATED)

                

        except:
            list=[]
            perfrom_data_list=[]
            data={
                'title':'',
                'url':'/',
                'created':'',
                'list':list,
                'item_list_data':perfrom_data_list,

            }
        return Response( data,status=status.HTTP_201_CREATED)

class Item_list_get_select_view_m(APIView):    

    def post(self,request):
      
      
            user_email = request.data['email']

            user_data = Marketer_user.objects.get(user_id = User.objects.get(email = user_email))
            item_succ = Item_succ.objects.filter(Marketer_id= user_data)
            succeded_list = []

            list = []

            

            for x in item_succ:
          
                if(x.userstate == True):
                    
                    succ_data ={
                        'url' : Items.objects.get(Item_title = x.Item_title).Item_url,
                        'Title' : Items.objects.get(Item_title = x.Item_title).Item_title
                    }
                
                    succeded_list.append(succ_data)

            data={ 
                'succeded_list':succeded_list
            } 
       
            

            return Response( data,status=status.HTTP_201_CREATED)   

class Submit_perform_m(APIView):

    def post(self,request):

        item_url = request.data['url']
        memo = request.data['memo']
        data_list = request.data['data_list']
        user_id =  Marketer_user.objects.get(user_id = User.objects.get(email = request.data['user']))
        item_id = Items.objects.get(Item_url = item_url)

        print(memo)

        perform = Perform_data.objects.create(
            Item_id_per=item_id,
            Marketer_id=user_id,
            memo=memo
        )

        for x in data_list:
            Perform_list.objects.create(
                Perform_id=perform,
                title = (list(x.keys())[0]),
                data=(list(x.values())[0]),
            )


        button_con = Button_con.objects.create(
            perform_id = perform,
        )

        Button_status.objects.create(
            button_id = button_con,
            title = '대기',
            color = 'outline-warning',
            value = 0
        )

        Button_status.objects.create(
            button_id = button_con,
            title = '승인',
            color = 'outline-success',
            value = 1
        )

        Button_status.objects.create(
            button_id = button_con,
            title = '반려',
            color = 'outline-danger',
            value = 2
        )

        Button_status.objects.create(
            button_id = button_con,
            title = '보완완료',
            color = 'outline-warning',
            value = 3
        )

        return Response( status=status.HTTP_201_CREATED)

class User_data_get(APIView):
        
    def post(self,request):
        
        email = request.data['email']
        
        data_list = []
        try:
            user = Marketer_user.objects.get(user_id = User.objects.get(email = email))

            data_list=[
            
            ['이메일',user.user_id.email],
        
            ['전화번호',user.phoneNumber],

            ['이름',user.user_id.name]
            ]
        except:
            print(email)
            user = Brand_user.objects.get(user_id = User.objects.get(nickname = email))
            
            data_list=[

            ['이메일',user.user_id.email],
        
            ['전화번호',user.phoneNumber],
         
            ['이름',user.user_id.name],

            ['사업자 등록번호',user.buisnessNumber],
       
            ]

        return Response(data_list, status=status.HTTP_201_CREATED)

class Marketer_is_data(APIView):

    def post(self,request):
        
        email = request.data['email']
        
        data_list = []

        user = Marketer_user.objects.get(user_id = User.objects.get(email = email))            
        m_user = Marketer_detail.objects.get(marketer_id = user)

        if(m_user.marketer_age != None and m_user.marketer_addr != None and m_user.marketer_job != None and m_user.marketer_career != None and m_user.marketer_form != None and m_user.marketer_plat != None):
    
            data_list=[
                ['나이',m_user.marketer_age],
                ['지역',m_user.marketer_addr],
                ['회사업종',m_user.marketer_job],
                ['경력 년수',m_user.marketer_career],
                ['참여 형식',m_user.marketer_form],
                ['플랫폼 실적',m_user.marketer_plat],
            ]
    
        return Response(data_list, status=status.HTTP_201_CREATED)

class Ai_model_log(APIView):

    def post(self,request):
        
        a_ver = Ai_version.objects.all()
        
        data_list = []

        for x in a_ver:

            data_list.append(
                {
               'ver_name' : x.ver_name,
                'ver_id' : x.ver_id,
                'updated_time' : x.updated_time,
                'count' : len(Brand_status.objects.filter(ver_id = x.ver_id))
                }
            )

        
        
        data = {
            'data_list' :data_list,
            'name' : data_list[-1]['ver_name'],
            'time' : data_list[-1]['updated_time'],
        } 


    
        return Response(data, status=status.HTTP_201_CREATED)

class User_data_get_op(APIView):

    def post(self,request):

        email = request.data['email']
        
        data_list = []
        try:
            user = Marketer_user.objects.get(user_id = User.objects.get(email = email))
            m_user = Marketer_detail.objects.get(marketer_id = user)

            data_list=[
            
                ['나이',m_user.marketer_age],
                ['지역',m_user.marketer_addr],
                ['회사업종',m_user.marketer_job],
                ['경력 년수',m_user.marketer_career],
                ['참여 형식',m_user.marketer_form],
                ['플랫폼 실적',m_user.marketer_plat],

            ]
        except:
            print(email)
            user = Brand_user.objects.get(user_id = User.objects.get(nickname = email))
            b_user = Brand_detail.objects.get(brand_id = user)



            data_list=[

            ['회사명',b_user.brand_name],
            ['주소',b_user.brand_addr],
            ['설립일',b_user.brand_date],
            ['매출액',b_user.brand_price],
            ['영업이익',b_user.brand_profit],
            ['신용등급 점수',b_user.brand_credit_grade_score],
            ['사원수',b_user.brand_employees],
            ['상세업종',b_user.brand_industry],
            ]

        return Response(data_list, status=status.HTTP_201_CREATED)

class User_data_edit(APIView):

    def post(self,request):

        email = request.data['email']
        data = request.data['data']



        try:
            user = Marketer_user.objects.get(user_id = User.objects.get(email = email))

            user.user_id.email = data[0]
            user.phoneNumber = data[1]
            user.user_id.name = data[2]
            user.user_id.save()
            user.save()



        except:
            user = Brand_user.objects.get(user_id = User.objects.get(nickname = email))

            user.user_id.email = data[0]
            user.phoneNumber = data[1]
            user.user_id.name = data[2]
            user.buisnessNumber = data[3]

            user.user_id.save()
            user.save()

        return Response( status=status.HTTP_201_CREATED)

class User_data_edit_op(APIView):

    def post(self,request):

        email = request.data['email']
        data = request.data['data']

        print(data)

        try:
            user = Marketer_user.objects.get(user_id = User.objects.get(email = email))

            try:
                m_user = Marketer_detail.objects.get(marketer_id = user)

                m_user.marketer_age = data[0]
                m_user.marketer_addr = data[1]
                m_user.marketer_job = data[2]
                m_user.marketer_career = data[3]
                m_user.marketer_form = data[4]
                m_user.marketer_plat = data[5]

                m_user.save()


            except:
                m_user = Marketer_detail.objects.create(
                    marketer_id = user,
                    marketer_age = data[0],
                    marketer_addr = data[1],
                    marketer_job = data[2],
                    marketer_career = data[3],
                    marketer_form = data[4],
                    marketer_plat = data[5],
                )
                m_user.save()

            # user.user_id.email = data[0]
            # user.phoneNumber = data[1]
            # user.user_id.name = data[2]
            # user.user_id.save()
            # user.save()

        except:
            user = Brand_user.objects.get(user_id = User.objects.get(nickname = email))
            b_user = Brand_detail.objects.get(brand_id = user)


            b_user.brand_name = data[0]
            b_user.brand_addr = data[1]
            b_user.brand_date = data[2]
            b_user.brand_price = data[3]
            b_user.brand_profit = data[4]
            b_user.brand_credit_grade_score = data[5]
            b_user.brand_employees = data[6]
            b_user.brand_industry = data[7]

     
            b_user.save()

        return Response( status=status.HTTP_201_CREATED)

class Get_memo(APIView):

    def post(self,request):

        id = request.data['id']


        pd = Perform_data.objects.get(pk = id)        
        
        pl = Perform_list.objects.filter(Perform_id = pd)

        memo = ''

        for x in pl :
            if x.title == 'memo':
                memo = x.data

        print(pd.memo)

        return Response( memo,status=status.HTTP_201_CREATED)

class Memo_edit(APIView):

    def post(self,request):

        id = request.data['id']
        memo = request.data['memo']

        pd = Perform_data.objects.get(pk = id)       

        pl = Perform_list.objects.filter(Perform_id = pd)

        for x in pl :
            if x.title == 'memo':
                x.data = memo
                x.save()

        return Response( status=status.HTTP_201_CREATED)

class Get_data(APIView):

    def post(self,request):

        id = request.data['id']
     


        pd = Perform_data.objects.get(pk = id)        
        pl = Perform_list.objects.filter(Perform_id =pd)

        for x in pl:
            if x.title == 'data':
                r_data = x.data

        return Response( r_data,status=status.HTTP_201_CREATED)

class Edit_data(APIView):

    def post(self,request):

        id = request.data['id']
        data = request.data['data']

        pd = Perform_data.objects.get(pk = id)        
        pl = Perform_list.objects.filter(Perform_id =pd)

        for x in pl:
            if x.title == 'data':
                x.data = data

                x.save() 

        return Response( status=status.HTTP_201_CREATED)



class Terms_data(APIView):

    def post(self,request):

        terms = Terms.objects.all()
        
        data =[]

        for x in terms:
            data.append({'eventKey':x.eventKey,'title':x.term_titleasd,'description':x.description})

        

        return Response( data, status=status.HTTP_201_CREATED)

class Region_change(APIView):

    def post(self,request):

        id = request.data['id']
        region = request.data['region']

        perform = Perform_data.objects.get(pk = id)
        
        perform_list = Perform_list.objects.filter(Perform_id = perform)

        for x in perform_list:
            if x.title == 'region':
                x.data = region
                x.save()

        return Response( status=status.HTTP_201_CREATED)