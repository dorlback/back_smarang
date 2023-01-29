import requests,sys,os,hashlib,hmac,base64,time,json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Test,Marketer,Brand,User,UserManager,Marketer_user,AuthSMS
import pandas as pd
from django.conf import settings
from pathlib import Path
import random as ran
import warnings
from rest_framework.generics import get_object_or_404 
from datetime import date
import re


class Check_sms(APIView):
    def get(self, request):
        try:
            p_num = request.query_params['phone_number']
            a_num = request.query_params['auth_number']


        except KeyError:
            return Response({'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            result = AuthSMS.check_auth_number(p_num, a_num)
            data={
                'result': result,
                'message': 'OK'

            }
            return Response(data,status=status.HTTP_201_CREATED)

    def post(self,request):
        
        phone_num = request.data['phone_number']
        phone_num =phone_num.replace("-","")

        
        print(phone_num)
        randnum = ran.randint(1000, 10000)        
        self = AuthSMS.objects
        # AuthSMS.send_sms(self,randnum,phone_num)
        AuthSMS.objects.update_or_create(phone_number=phone_num)
        return Response( status=status.HTTP_201_CREATED)
        


        # timestamp = int(time.time() * 1000)
        # timestamp = str(timestamp)

        # access_key = "6a9pS5ADEIHjJ2ihSPHK"
        # secret_key = "TjU5TOqoxFqflUtOG8Ynhw8GkxSbQrCnaSPJqYTwTjU5TOqoxFqflUtOG8Ynhw8GkxSbQrCnaSPJqYTw"


        # url = "https://sens.apigw.ntruss.com"
        # uri = "/sms/v2/services/ncp:sms:kr:292768866528:sms_auth/messages"

        # def	make_signature():
        #     timestamp = int(time.time() * 1000)
        #     timestamp = str(timestamp)

        #     access_key = "6a9pS5ADEIHjJ2ihSPHK"				# access key id (from portal or Sub Account)
        #     secret_key = "TjU5TOqoxFqflUtOG8Ynhw8GkxSbQrCnaSPJqYTw"				# secret key (from portal or Sub Account)
        #     secret_key = bytes(secret_key, 'UTF-8')

        #     method = "POST"
        #     uri = "/sms/v2/services/ncp:sms:kr:292768866528:sms_auth/messages"

        #     message = method + " " + uri + "\n" + timestamp + "\n" + access_key
        #     message = bytes(message, 'UTF-8')
        #     signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        #     return signingKey

        

        # header = {
        #         "Content-Type": "application/json; charset=utf-8",
        #         "x-ncp-apigw-timestamp": timestamp,
        #         "x-ncp-iam-access-key": access_key,
        #         "x-ncp-apigw-signature-v2": make_signature()
        #     }
        
        # data = {
        #     "type":"SMS",
        #     "contentType":"COMM",
        #     "countryCode":"82",
        #     "from":"01055777810",
        #     "content":"5840",
        #     "messages":[
        #         {
        #             "to":"01055777810",
        #             "subject":"[인증번호]",
        #             "content":"[인증번호]5840"
        #         }
        #     ]
        # }

        # res = requests.post("https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:292768866528:sms_auth/messages",headers=header,data=json.dumps(data))
        # print(res.text)
        # return Response( status=status.HTTP_201_CREATED)