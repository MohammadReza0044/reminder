from turtle import title
from django.shortcuts import render , redirect
from django.views import View


from .models import Reminder
from .forms import ReminderForm


class reminder_list(View):
    template_name = 'reminder/reminder_list.html'

    def get(self,request):
        reminder = Reminder.objects.all()
        context = {'reminder': reminder}
        return render (request, self.template_name, context=context)



def create_reminder(request):
        form = ReminderForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title'] 
            message = form.cleaned_data ['message'] 
            reminder_date = form.cleaned_data ['reminder_date'] 
            reminder_time = form.cleaned_data ['reminder_time'] 
            form.save()
            return redirect ('/reminder')

        return render(request, 'reminder/reminder_add.html', {'form': form})