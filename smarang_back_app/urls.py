from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views.Ai_views import Ai_test,Marketer_getgrade,Brand_getgrade,Marketer_getBrand,Brand_getMarketer,Marketer_create_data,Ai_delete
from .views.Test_views import Ai_model_log,Marketer_is_data,User_data_edit_op,User_data_get_op,Region_change,Item_perform_del,Marketer_list_search_get,Item_list_get_view_search_m,Item_list_get_search_view,Terms_data,User_create,Edit_data,Memo_edit,Get_memo,Get_data,Marketer_create,User_data_edit,Login_view,Item_list_get_view,Item_list_get_select_view_m,User_data_get,Submit_perform_m,Item_list_get_view_m,Brand_create,Marketer_subscribe_create,Marketer_Market_list,Marketer_list_get,Marketer_state_change
from .views.Sms_views import Check_sms
from .views.Cal_views import Cal_create_get_list,Cal_create_get_p_inner,Cal_data_get_p_inner,Cal_data_get,Cal_data_list_get,Cal_data_get_p,Cal_innder_list_get,Cal_inner_data_create,Cal_inner_data_edit,Handle_edit_cal_inner,Cal_create
from .views.Review_views import Button_data_get,Button_data_save
from .views.File_views import POST_create,POST_get,Delete_img
from .views.Notice_views import Notice_data_get,Notice_inner_get
from . import views


urlpatterns = [
    path('Ai_data/',Ai_test.as_view()),   
    path('M_grade/',Marketer_getgrade.as_view()), 
    path('B_get/',Brand_getMarketer.as_view()), 
    path('M_get/',Marketer_getBrand.as_view()), 
    path('B_grade/',Brand_getgrade.as_view()),
    path('User_create/',User_create.as_view()),
    path('m_user_create/',Marketer_create.as_view()),
    path('m_sub_create/',Marketer_subscribe_create.as_view()),
    path('b_user_create/',Brand_create.as_view()),
    path('check/',Check_sms.as_view()),
    path('Login/',Login_view.as_view()),
    path('item_data_get/',Item_list_get_view.as_view()),
    path('item_data_search_get/',Item_list_get_search_view.as_view()),
    path('marketer_market_get/',Marketer_Market_list.as_view()),
    path('marketer_state_change/',Marketer_state_change.as_view()),

    path('Item_list_get_select_view_m/',Item_list_get_select_view_m.as_view()),

    path('item_list_get_view_search_m/',Item_list_get_view_search_m.as_view()),
    
    path('ai_model_log/',Ai_model_log.as_view()),

    path('user_data_get_op/',User_data_get_op.as_view()),
    path('user_data_get/',User_data_get.as_view()),
    path('marketer_is_data/',Marketer_is_data.as_view()),

    path('marketer_create_data/',Marketer_create_data.as_view()),


    path('ai_delete/',Ai_delete.as_view()),
    path('memo_edit/',Memo_edit.as_view()),
    path('get_memo/',Get_memo.as_view()),
    path('get_data/',Get_data.as_view()),
    path('edit_data/',Edit_data.as_view()),

    path('region_change/',Region_change.as_view()),
    

    path('user_data_edit/',User_data_edit.as_view()),
    path('user_data_edit_op/',User_data_edit_op.as_view()),
    
    
    path('brand_marketer_search_get/',Marketer_list_search_get.as_view()),
    path('brand_marketer_get/',Marketer_list_get.as_view()),

    path('submit_perform_m/',Submit_perform_m.as_view()),
    path('item_data_get_m/',Item_list_get_view_m.as_view()),
    path('cal_data_list/',Cal_data_list_get.as_view()),
    path('get_cal_data/',Cal_data_get.as_view()),

    path('cal_inner_list_get/',Cal_innder_list_get.as_view()),
    path('cal_inner_data_create/',Cal_inner_data_create.as_view()),
    path('cal_inner_data_edit/',Cal_inner_data_edit.as_view()),
    path('handle_edit_cal_inner/',Handle_edit_cal_inner.as_view()),
    path('cal_create/',Cal_create.as_view()),
    path('cal_data_get_p/',Cal_data_get_p.as_view()),
    path('cal_data_get_p_inner/',Cal_data_get_p_inner.as_view()),
    path('cal_create_get_p_inner/',Cal_create_get_p_inner.as_view()),
    path('cal_create_get_list/',Cal_create_get_list.as_view()),
    
    path('post_create/',POST_create.as_view()),
    path('post_get/',POST_get.as_view()),
    path('delete_img/',Delete_img.as_view()),


    path('item_perform_del/',Item_perform_del.as_view()),
    


    path('button_data_get/',Button_data_get.as_view()),
    path('button_data_save/',Button_data_save.as_view()),

    path('notice_data_get/',Notice_data_get.as_view()),
    path('notice_inner_get/',Notice_inner_get.as_view()),

    path('terms_data/',Terms_data.as_view()),
    
    

    
    

]

