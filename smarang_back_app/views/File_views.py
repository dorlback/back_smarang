from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import POST,Marketer,Brand,User,UserManager,Marketer_user,Brand_user,Cal_table,Marketer_user,Cal_data,AuthSMS,Items,Item_list,Perform_data,Perform_list,Item_succ
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



class POST_create(APIView):

    def post(self,request):
        
        

        data = request.data
        id = request.data.get('id')


        for x in data:
  
            if x != 'id':
                POST.objects.create(
                        perform_id = Perform_data.objects.get(pk = id),
                        photo = request.data[x]
                    )

        
        
        return Response( status=status.HTTP_201_CREATED)

class POST_get(APIView):

    def post(self,request):
        
        
        id = request.data.get('id')

        perform_id = Perform_data.objects.get(pk = id)

        post =POST.objects.filter(perform_id = perform_id)
        
        img_list = []

        for x in post:
            img_list.append('/media/'+str(x.photo))

        
        
        
        return Response(img_list, status=status.HTTP_201_CREATED)