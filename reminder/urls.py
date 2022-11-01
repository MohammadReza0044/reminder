from django.urls import path 
from .views import reminder_list, reminder_detail, delete, rimender_Update

urlpatterns = [
    path('', reminder_list.as_view(), name='reminder_list'),
    path('/<pk>', reminder_detail.as_view(), name='reminder_detail' ),
    path('/delete/<pk>', delete, name='reminder_delete' ),
    path('/update/<pk>', rimender_Update.as_view(), name='reminder_update' ),
    
]
