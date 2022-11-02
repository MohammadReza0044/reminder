from django.shortcuts import render , redirect , get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse_lazy
import datetime

from .models import Reminder
from .forms import ReminderForm



class reminder_list(View):
    template_name = 'reminder/reminder_list.html'

    def get(self,request):
        today = datetime.date.today()
        near_reminder = Reminder.objects.filter(show_date = today).order_by('reminder_date')
        context = {'near_reminder':near_reminder}
        return render (request, self.template_name, context=context)
    
    def post (self,request):
        form = ReminderForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title'] 
            message = form.cleaned_data ['message'] 
            reminder_date = form.cleaned_data ['reminder_date'] 
            show_date = form.cleaned_data ['show_date'] 
            form.save()
        return redirect('/')


class reminder_detail(View):
    template_name = 'reminder/reminder_detail.html'

    def get(self,request,pk):
        reminder = get_object_or_404(Reminder, pk=pk)
        context = {'reminder': reminder}
        return render (request, self.template_name, context=context)

class reminder_total_list(View):
    template_name = 'reminder/reminder_total_list.html'

    def get(self,request):
        reminder = Reminder.objects.all().order_by('reminder_date')
        context = {'reminder': reminder}
        return render (request, self.template_name, context=context)


class reminder_Delete(DeleteView):
    model = Reminder
    success_url = reverse_lazy('reminder:reminder_list')



class rimender_Update(UpdateView):
    model = Reminder
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('reminder:reminder_list')