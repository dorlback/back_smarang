from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Test,Marketer,Brand,Terms,User,UserManager,Marketer_user,Brand_user,Button_con,Cal_table,Button_status,Marketer_user,Cal_data,AuthSMS,Items,Item_list,Perform_data,Perform_list,Item_succ
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

        Marketer_user.objects.create(
            user_id = user,
            phoneNumber= request.data['phone_number'].replace("-",""),
        )
        
        return Response( status=status.HTTP_201_CREATED)   

        

class Marketer_subscribe_create(APIView):

    def post(self,request):
        
        email = request.data['email']
        print(email)

        applicate = Item_succ.objects.create(
            Marketer_id = Marketer_user.objects.get(user_id = User.objects.get(email = email)),
            Item_title = 'SCRM',
            Item_id_per = Items.objects.get(Item_title='SCRM')
        )
        
        return Response( status=status.HTTP_201_CREATED)  

                                                                                         
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

        Brand_user.objects.create( 
            user_id = user,
            phoneNumber= request.data['phone_number'].replace("-",""),
            buisnessNumber = request.data['buisnessNumber']
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
            title = '보안완료',
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