from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.validators import RegexValidator
import datetime
from django.utils import timezone
from random import randint
import requests
import time,base64,hmac,hashlib,json
from ckeditor_uploader.fields import RichTextUploadingField 

class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, nickname, password,name):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname     ,  
            name = name 
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        


        return user     
        


    def create_superuser(self, email, nickname,password ):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        

        

        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 
    
    def check_password(self, password):
        print(password)
        print(self.password)

        if(password == self.password):
            print('맞음')

        else:
            print('아님')

        return(True)

          
    
class User(AbstractBaseUser,PermissionsMixin):    
    
    objects = UserManager()

    email = models.EmailField(
        max_length=255,        
        unique=True,    
    )
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )     
    name = models.CharField(
        max_length=20,
        null=True,
    )  
    password = models.CharField(
        max_length=100,
        null=False,
        unique=False
    )

    
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'nickname'    
    REQUIRED_FIELDS = ['email']



class Brand_user(models.Model):
    user_id = models.ForeignKey("User", related_name='user_b',on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = False)
    buisnessNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

class Marketer_user(models.Model):
    user_id = models.ForeignKey("User", related_name='user_m',on_delete=models.CASCADE)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = False)


class BrandAbstract(models.Model):
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

    class Meta:
        abstract = True
        
    

class Brand(BrandAbstract):
    updated_time = models.DateField(auto_now=False)
    ver_id = models.IntegerField(default=-1)



class Brand_status(models.Model):
    brand_id = models.ForeignKey("Brand_raw", related_name="brand_id_d", on_delete=models.CASCADE)
    ver_id = models.IntegerField(default=-1)

class Brand_dummy(models.Model):
    brand_id = models.ForeignKey("Brand_raw", related_name="brand_id", on_delete=models.CASCADE)


class Ai_version(models.Model):
    ver_name = models.CharField(max_length=50) #나이
    ver_id = models.IntegerField()
    updated_time = models.DateField(auto_now=True)


class Brand_raw(BrandAbstract):
    pass


class Brand_back_up(BrandAbstract):
    pass

class Marketer(models.Model):

    marketer_age = models.CharField(max_length=50) #나이
    marketer_addr = models.CharField(max_length=50) #지역
    marketer_job = models.CharField(max_length=50) #직업경력
    marketer_career = models.CharField(max_length=50) #경력년수
    marketer_form = models.CharField(max_length=50) #참여형식
    marketer_plat = models.CharField(max_length=50) #플랫폼실적
    marketer_pow = models.CharField(max_length=50) #마케터파워지수
    marketer_grade = models.CharField(max_length=50) #등급

class Brand_detail(models.Model):
    brand_id = models.ForeignKey("Brand_user", related_name='brand_u',on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=50,blank=True,null=True,) #회사명
    brand_addr = models.CharField(max_length=50) #주소
    brand_date = models.CharField(max_length=50) #설립일
    brand_price = models.CharField(max_length=50) #매출액
    brand_profit = models.CharField(max_length=50) #영업이익
    brand_credit_grade_score = models.CharField(max_length=50) #신용등급_점수
    brand_employees = models.CharField(max_length=50) #사원수
    brand_industry = models.CharField(max_length=50) #상세업종



class Marketer_detail(models.Model):
    marketer_id = models.ForeignKey("Marketer_user", related_name='marketer_u',on_delete=models.CASCADE)
    marketer_age = models.CharField(max_length=50,null=True,blank=True) #나이
    marketer_addr = models.CharField(max_length=50,null=True,blank=True) #지역
    marketer_job = models.CharField(max_length=50,null=True,blank=True) #회사업종
    marketer_career = models.CharField(max_length=50,null=True,blank=True) #경력년수
    marketer_form = models.CharField(max_length=50,null=True,blank=True) #참여형식
    marketer_plat = models.CharField(max_length=50,null=True,blank=True) #플랫폼실적


class Test(models.Model):
    marketer_age = models.CharField(max_length=50) #나이
    marketer_addr = models.CharField(max_length=50) #지역
    marketer_job = models.CharField(max_length=50) #직업경력
    marketer_career = models.CharField(max_length=50) #경력년수
    marketer_form = models.CharField(max_length=50) #참여형식
    marketer_plat = models.CharField(max_length=50) #플랫폼실적
    marketer_pow = models.CharField(max_length=50) #마케터파워지수
    marketer_grade = models.CharField(max_length=50) #등급

class Item_succ(models.Model):

    userstate = models.BooleanField(default=False)
    Item_title = models.CharField(max_length=50)
    Item_id_per = models.ForeignKey("Items",related_name='item_id_perform_succ',on_delete=models.CASCADE)
    Marketer_id = models.OneToOneField("Marketer_user",related_name='Marketer_user_succ',on_delete=models.CASCADE)



class AuthSMS(TimeStampedModel):


    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, primary_key=True)
    auth_number = models.IntegerField(verbose_name='인증 번호')
    # auth_pass = models.CharField(max_length=50, null=True ,blank=True)
    
    class Meta:
        db_table = 'authsms'

    def save(self, *args, **kwargs):
        self.auth_number = randint(1000, 10000)
        self.phone_number = self.phone_number
        super().save(*args, **kwargs)
        self.send_sms(self.auth_number,self.phone_number)  # 인증번호가 담긴 SMS를 전송

        
        
    def send_sms(self,auth_number,phone_number):
        self.auth_number = auth_number
        self.phone_number = phone_number

        timestamp = int(time.time() * 1000)
        timestamp = str(timestamp)

        access_key = "6a9pS5ADEIHjJ2ihSPHK"
        secret_key = "TjU5TOqoxFqflUtOG8Ynhw8GkxSbQrCnaSPJqYTwTjU5TOqoxFqflUtOG8Ynhw8GkxSbQrCnaSPJqYTw"
        
        url = "https://sens.apigw.ntruss.com"
        uri = "/sms/v2/services/ncp:sms:kr:292768866528:sms_auth/messages"

        def	make_signature():
            timestamp = int(time.time() * 1000)
            timestamp = str(timestamp)

            access_key = "6a9pS5ADEIHjJ2ihSPHK"				# access key id (from portal or Sub Account)
            secret_key = "TjU5TOqoxFqflUtOG8Ynhw8GkxSbQrCnaSPJqYTw"				# secret key (from portal or Sub Account)
            secret_key = bytes(secret_key, 'UTF-8')

            method = "POST"
            uri = "/sms/v2/services/ncp:sms:kr:292768866528:sms_auth/messages"

            message = method + " " + uri + "\n" + timestamp + "\n" + access_key
            message = bytes(message, 'UTF-8')
            signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
            return signingKey

        header = {
                "Content-Type": "application/json; charset=utf-8",
                "x-ncp-apigw-timestamp": timestamp,
                "x-ncp-iam-access-key": access_key,
                "x-ncp-apigw-signature-v2": make_signature()
            }

        data = {
            "type":"SMS",
            "contentType":"COMM",
            "countryCode":"82",
            "from":"01055777810",
            "content":"[인증번호]"+str(auth_number),
            "messages":[
                {
                    "to":phone_number,
                    "subject":"[인증번호]",
                    "content":"[인증번호]"+str(auth_number),
                }
            ]
        }

        res = requests.post("https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:292768866528:sms_auth/messages",headers=header,data=json.dumps(data))
        print(auth_number)
        return(res.text)

        

    @classmethod
    def check_auth_number(cls, p_num, c_num):
        print(c_num)
        time_limit = timezone.now() - datetime.timedelta(minutes=3)
        result = cls.objects.filter(
            phone_number=p_num,
            auth_number=c_num,
            modified_time__gte=time_limit
        )
        if result:
            return True
        return False

        

class Items(models.Model):
    Brand_user_id = models.ForeignKey("Brand_user",related_name='Brand_user_id',on_delete=models.CASCADE)
    Item_title = models.CharField(max_length=50,unique = True) 
    Item_url = models.CharField(max_length=50,unique = True) 
    created_at = models.DateTimeField(auto_now_add=True)   


class Item_list(models.Model):
    Title = models.CharField(max_length=50)
    Item_id = models.ForeignKey("Items",related_name='item_id',on_delete=models.CASCADE)

    

class Perform_data(models.Model):
    cal_id = models.ForeignKey("Cal_data",related_name='cal_id_perform',on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    Item_id_per = models.ForeignKey("Items",related_name='item_id_perform',on_delete=models.CASCADE)
    Marketer_id = models.ForeignKey("Marketer_user",related_name='Marketer_user',on_delete=models.CASCADE)
    memo = models.TextField(null=True,blank=True)

    

class UploadFileModel(models.Model):
    perform_id = models.ForeignKey("Perform_data",related_name='perform_id_file',on_delete=models.CASCADE)
    title = models.TextField(default='')
    file = models.FileField(null=True,blank=True)

class Button_con(models.Model):
    perform_id = models.ForeignKey("Perform_data",related_name='perform_id_btn',on_delete=models.CASCADE)
    button_state = models.CharField(max_length=10,default='정상')
    memo = models.TextField(null=True,blank=True)

class Button_status(models.Model):
    button_id = models.ForeignKey("Button_con", related_name='button_con_id',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50,null=True,blank=True)
    value = models.CharField(max_length=50,null=True,blank=True)

    
class Perform_list(models.Model):
    Perform_id = models.ForeignKey("Perform_data",related_name='perform_id',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    data = models.CharField(max_length=50,null=True,blank=True)

class Cal_table(models.Model):
    item_id = models.ForeignKey("Items",related_name='item_id_cal',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class Cal_data(models.Model):
    cal_id = models.ForeignKey("Cal_table",related_name='cal_id',on_delete=models.CASCADE)
    cal_title = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)    
    described = models.CharField(max_length=50)


class POST(models.Model):
    perform_id = models.ForeignKey("Perform_data",related_name='perform_id_post',on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='post/')
	# (1) 저장경로 : MEDIA_ROOT/blog/post/xxx.png
    	#     DB필드 : MEDIA_URL/blog/post/xxx.png' 문자열 저장

    
	# (2) 저장경로 : MEDIA_ROOT/blog/post/20210901/xxx.png
    	#     DB필드 :  'MEDIA_URL/blog/post/20210901/xxx.png' 문자열 저장
	

class Notice(models.Model):
    notice_title = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True) 
    description =RichTextUploadingField() # CKEditor Rich Text Field

    def __str__(self):
        return self.notice_title


class Terms(models.Model):
    eventKey = models.CharField(max_length=50)
    term_titleasd = models.CharField(max_length=50)
    description =RichTextUploadingField() # CKEditor Rich Text Field

    def __str__(self):
        return self.term_titleasd