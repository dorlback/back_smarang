from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Button_con,Button_status,Brand,User,UserManager,Marketer_user,Brand_user,Cal_table,Marketer_user,Cal_data,AuthSMS,Items,Item_list,Perform_data,Perform_list,Item_succ
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

 

class Button_data_get(APIView):

    def post(self,request):

  

        id = request.data['id']

        button_con = Button_con.objects.get(perform_id = id)
        button_status = Button_status.objects.filter(button_id= button_con)
        radios = []
        for x in button_status:
            radios.append({ 'name': x.title, 'value': x.value,'color': x.color })
            if x.title == button_con.button_state:
                button_status=x.value
        
        data={
            'memo': button_con.memo,
            'radios':radios,
            'status':str(button_status)
        }

        
        return Response(data, status=status.HTTP_201_CREATED)

class Button_data_save(APIView):

    def post(self,request):

  
        id = request.data['id']

        state = request.data['status']
        memo = request.data['memo']

        print(state)

        perform = Perform_data.objects.get(pk = id)
        perform_list = Perform_list.objects.filter(Perform_id = perform)
        button_con = Button_con.objects.get(perform_id = id)
        button_status = Button_status.objects.filter(button_id= button_con)

        for x in perform_list:
            
            if x.title == 'button' :
       
                x.data = Button_status.objects.get(value= state).title
                x.save()

        

        for x in button_status:
            if x.value == state:
                button_status=x.title

        button_con.button_state = button_status
        button_con.memo = memo
        button_con.save()
        

        

        return Response( status=status.HTTP_201_CREATED)