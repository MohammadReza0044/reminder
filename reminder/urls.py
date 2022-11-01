from django.urls import path 
from .views import reminder_list, create_reminder

urlpatterns = [
    path('', reminder_list.as_view(), name='reminder_list'),
    path('/add_reminder', create_reminder , name='new_reminder'),
]
