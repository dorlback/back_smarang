from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Test,Marketer,Brand,User,UserManager,Marketer_user,Brand_user,Cal_table,Marketer_user,Cal_data,AuthSMS,Items,Item_list,Perform_data,Perform_list,Item_succ
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


warnings.filterwarnings('ignore')



class Cal_data_get(APIView):

    def post(self,request):

  
        email = request.data['email']
     

        Item_data = Items.objects.filter(Brand_user_id=Brand_user.objects.get(user_id = User.objects.get(nickname = email)))

     

        url_list = []

        for x in Item_data:
            url_list.append(x.Item_url)

        


        return Response( url_list,status=status.HTTP_201_CREATED)


class Cal_data_list_get(APIView):

    def post(self,request):

        url = request.data['url']
    
        

        Item_data = Items.objects.get(Item_url = url)

        cal_table = Cal_table.objects.filter(item_id = Item_data)

        cal_list = []

        for x in cal_table:
            
            cal_list.append([x.title,x.id])


        return Response( cal_list,status=status.HTTP_201_CREATED)




class Cal_innder_list_get(APIView):

    def post(self,request):

        id = request.data['id']
    
        cal_table = Cal_table.objects.get(pk = id)

        cal_data = Cal_data.objects.filter(cal_id = cal_table)

        cal_data_list = []

        for x in cal_data:
            data={
                'title' : x.cal_title,
                'described':x.described,
                'date':x.date_joined,
                'id':x.id
            }
            cal_data_list.append(data)

        return Response(cal_data_list, status=status.HTTP_201_CREATED)



class Cal_inner_data_create(APIView):

    def post(self,request):

        id = request.data['id']
        title = request.data['title']
        described = request.data['described']
        cal_table = Cal_table.objects.get(pk = id)

        cal=Cal_data.objects.create(
            cal_id = cal_table,
            cal_title = title,
            described = described
        )
        print(cal)

        cal.save()

        return Response( status=status.HTTP_201_CREATED)

class Cal_inner_data_edit(APIView):

    def post(self,request):
        print(request.data)
        id = request.data['id']
        title = request.data['title']

        
        cal_table = Cal_table.objects.get(pk = id)

        cal_table.title = title
        

        cal_table.save()

        return Response( status=status.HTTP_201_CREATED)

class Handle_edit_cal_inner(APIView):

    def post(self,request):
        
        id = request.data['id']
        title = request.data['title']
        described = request.data['described']
                
        cal_data = Cal_data.objects.get(pk = id)

        cal_data.title = title
        cal_data.described = described
        

        cal_data.save()

        return Response( status=status.HTTP_201_CREATED)

class Cal_create(APIView):

    def post(self,request):
        
        url = request.data['url']
        title = request.data['title']

        item = Items.objects.get(Item_url = url)
        cal_table = Cal_table.objects.create(
            item_id = item,
            title = title
        )


        cal_table.save()

        return Response( status=status.HTTP_201_CREATED)

class Cal_data_get_p(APIView):

    def post(self,request):
        
        url = request.data['url']

        cal = Cal_table.objects.filter(item_id = Items.objects.get(Item_url = url))

        list = []

        for x in cal:
            list.append({
                'title':x.title,
                'id':x.id
            })

        return Response( list,status=status.HTTP_201_CREATED)


class Cal_data_get_p_inner(APIView):

    def post(self,request):
        
        id = request.data['id']

        cal = Cal_data.objects.filter(cal_id = Cal_table.objects.get(pk = id))

        list = []

        for x in cal:
            list.append({
                'title':x.cal_title,
                'id':x.id,
                'described':x.described
            })

        return Response( list,status=status.HTTP_201_CREATED)


class Cal_create_get_p_inner(APIView):

    def post(self,request):
        
        id = request.data['id']
        per_list = request.data['per_list']

        print(id)

        cal = Cal_data.objects.get(pk=id)

        for x in per_list:
            perform = Perform_data.objects.get(pk = x)
            perform.cal_id = cal
            perform.save()

        return Response( status=status.HTTP_201_CREATED)


class Cal_create_get_list(APIView):

    def post(self,request):
        
        id = request.data['id']

        print(id)
        
        perform = Perform_data.objects.get(pk = id)

        perform.cal_id.date_joined
        
        
        return Response(perform.cal_id.date_joined, status=status.HTTP_201_CREATED)