from django.shortcuts import render , redirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
import datetime

from .models import Reminder



class reminder_list(View):
    template_name = 'reminder/reminder_list.html'

    def get(self,request):
        reminder = Reminder.objects.all()
        today = datetime.date.today()
        near_reminder = Reminder.objects.filter(show_date = today)
        context = {'reminder': reminder, 'near_reminder':near_reminder}
        return render (request, self.template_name, context=context)
    
    def post (self,request):
        new_reminder = Reminder.objects.create(
            title = request.POST.get('title'),
            message = request.POST.get('message'),
            reminder_date = request.POST.get('reminder_date'),
            show_date = request.POST.get('show_date'),
        )
        new_reminder.save()
        return redirect('/')


class reminder_detail(View):
    template_name = 'reminder/reminder_detail.html'

    def get(self,request,pk):
        reminder = Reminder.objects.filter(pk=pk)
        context = {'reminder': reminder}
        return render (request, self.template_name, context=context)

class reminder_total_list(View):
    template_name = 'reminder/reminder_total_list.html'

    def get(self,request):
        reminder = Reminder.objects.all().order_by('reminder_date')
        context = {'reminder': reminder}
        return render (request, self.template_name, context=context)

def delete(request,pk):
        reminder = Reminder.objects.filter(pk=pk)
        reminder.delete()
        return redirect ('/')


class rimender_Update(UpdateView):
    model = Reminder
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('reminder:reminder_list')