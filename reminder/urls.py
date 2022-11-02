from django.urls import path 
from .views import reminder_list, reminder_detail, reminder_Delete, rimender_Update, reminder_total_list

urlpatterns = [
    path('', reminder_list.as_view(), name='reminder_list'),
    path('reminders', reminder_total_list.as_view(), name='reminder_total'),
    path('<int:pk>', reminder_detail.as_view(), name='reminder_detail' ),
    path('/delete/<int:pk>', reminder_Delete.as_view(), name='reminder_delete' ),
    path('/update/<int:pk>', rimender_Update.as_view(), name='reminder_update' ),
    
]
