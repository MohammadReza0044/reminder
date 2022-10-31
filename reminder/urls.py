from django.urls import path 
from .views import reminder_list

urlpatterns = [
    path('', reminder_list.as_view(), name='reminder_list'),
]
