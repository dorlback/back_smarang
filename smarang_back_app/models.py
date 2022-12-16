from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=50,blank=True,null=True,) #회사명
    brand_addr = models.CharField(max_length=50) #주소
    brand_date = models.CharField(max_length=50) #설립일
    brand_scale = models.CharField(max_length=50) #기업규모
    brand_shape = models.CharField(max_length=50) #기업형태
    brand_price = models.CharField(max_length=50) #매출액
    brand_profit = models.CharField(max_length=50) #영업이익
    brand_profit_loss = models.CharField(max_length=50) #당기손익
    brand_credit_grade = models.CharField(max_length=50) #신용등급
    brand_credit_grade_score = models.CharField(max_length=50) #신용등급_점수
    brand_employees = models.CharField(max_length=50) #사원수
    brand_industry = models.CharField(max_length=50) #상세업종
    brand_Needs = models.CharField(max_length=50) #니즈지수
    brand_grade = models.CharField(max_length=50) #등급

class Test(models.Model):
    marketer_age = models.CharField(max_length=50) #나이
    marketer_addr = models.CharField(max_length=50) #지역
    marketer_job = models.CharField(max_length=50) #직업경력
    marketer_career = models.CharField(max_length=50) #경력년수
    marketer_form = models.CharField(max_length=50) #참여형식
    marketer_plat = models.CharField(max_length=50) #플랫폼실적
    marketer_pow = models.CharField(max_length=50) #마케터파워지수
    marketer_grade = models.CharField(max_length=50) #등급

class Marketer(models.Model):
    marketer_age = models.CharField(max_length=50) #나이
    marketer_addr = models.CharField(max_length=50) #지역
    marketer_job = models.CharField(max_length=50) #직업경력
    marketer_career = models.CharField(max_length=50) #경력년수
    marketer_form = models.CharField(max_length=50) #참여형식
    marketer_plat = models.CharField(max_length=50) #플랫폼실적
    marketer_pow = models.CharField(max_length=50) #마케터파워지수
    marketer_grade = models.CharField(max_length=50) #등급