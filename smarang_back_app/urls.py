from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Ai_test,Marketer_getgrade,Brand_getgrade,Marketer_getBrand
from . import views

urlpatterns = [
    path('Ai_data/',Ai_test.as_view()),   
    path('M_grade/',Marketer_getgrade.as_view()), 
    path('M_get/',Marketer_getBrand.as_view()), 
    path('B_grade/',Brand_getgrade.as_view()), 
]

