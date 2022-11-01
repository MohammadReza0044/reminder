from typing import Optional
from django.shortcuts import render , redirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import Reminder



class reminder_list(View):
    template_name = 'reminder/reminder_list.html'

    def get(self,request):
        reminder = Reminder.objects.all()
        context = {'reminder': reminder}
        return render (request, self.template_name, context=context)
    
    def post (self,request):
        new_reminder = Reminder.objects.create(
            title = request.POST.get('title'),
            message = request.POST.get('message'),
            reminder_date = request.POST.get('reminder_date'),
            reminder_time = request.POST.get('reminder_time'),
        )
        new_reminder.save()
        return redirect('/reminder')


class reminder_detail(View):
    template_name = 'reminder/reminder_detail.html'

    def get(self,request,pk):
        reminder = Reminder.objects.filter(pk=pk)
        context = {'reminder': reminder}
        return render (request, self.template_name, context=context)

    def post(self,request,pk):
        updated_reminder = Reminder.objects.filter(pk=pk)

        updated_reminder.title = request.POST.get('title'),
        updated_reminder.message = request.POST.get('message'),
        updated_reminder.reminder_date = request.POST.get('reminder_date'),
        updated_reminder.reminder_time = request.POST.get('reminder_time'),
        
        updated_reminder.save()
        return redirect('/reminder')

   

def delete(request,pk):
        reminder = Reminder.objects.filter(pk=pk)
        reminder.delete()
        return redirect ('/reminder')


class rimender_Update(UpdateView):
    model = Reminder
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('reminder:reminder_list')