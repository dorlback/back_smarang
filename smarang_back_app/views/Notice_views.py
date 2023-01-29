from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Button_con,Button_status,Notice,Brand,User,UserManager,Marketer_user,Brand_user,Cal_table,Marketer_user,Cal_data,AuthSMS,Items,Item_list,Perform_data,Perform_list,Item_succ
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

 

class Notice_data_get(APIView):

    def post(self,request):

        notice = Notice.objects.all()

        data = []

        for x in notice:
            data.append({'title':x.notice_title , 'date':x.date_joined,'id':x.id})

        
        return Response(data, status=status.HTTP_201_CREATED)


class Notice_inner_get(APIView):

    def post(self,request):

        id = request.data['id']

        notice = Notice.objects.get(pk = id)


        print(notice.description)

        data= {'title':notice.notice_title , 'date':notice.date_joined,'id':notice.id,'description':notice.description}

        
        return Response(data, status=status.HTTP_201_CREATED)
