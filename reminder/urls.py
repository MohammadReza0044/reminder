from django.urls import path 
from .views import reminder_list, reminder_detail, delete, rimender_Update, reminder_total_list

urlpatterns = [
    path('', reminder_list.as_view(), name='reminder_list'),
    path('reminders', reminder_total_list.as_view(), name='reminder_total'),
    path('<pk>', reminder_detail.as_view(), name='reminder_detail' ),
    path('/delete/<pk>', delete, name='reminder_delete' ),
    path('/update/<pk>', rimender_Update.as_view(), name='reminder_update' ),
    
]
