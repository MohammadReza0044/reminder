from django.shortcuts import render
from django.views import View


from .models import Reminder


class reminder_list(View):
    def get(self,request):
        reminder = Reminder.objects.all()
        context = {'reminder': reminder}
        return render (request,'reminder/reminder_list.html', context=context)