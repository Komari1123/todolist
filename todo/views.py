from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView,TemplateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .lib import TimeScheduleBS4
from django.db.models import Sum


def timer(request):
    user = request.user.pk
    object_list = TodoModel.objects.filter(author_pk=user)

    if request.method == 'POST':
        radio = request.POST['radio1']
        post = TodoModel.objects.get(pk=radio)
        post.true_pomodoro = post.true_pomodoro + 1
        post.save()

        radio = request.POST['radio2']
        if radio == 're':
            return redirect('timer')
        elif radio == 'home':
            return redirect('list')
    return render(request, 'timer.html',{'object_list':object_list})

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

    def get_context_data(self, *args, **kwargs):
        user = self.request.user.pk
        todomodel = TodoModel.objects.filter(author_pk=user)
        sum_pre = todomodel.aggregate(Sum('predict_pomodoro'))
        sum_true = todomodel.aggregate(Sum('true_pomodoro'))
        sum_count = todomodel.count()

        schedules = todomodel.order_by('start_time')
        time_schedule = TimeScheduleBS4(step=10, minute_height=0.5)
        context = super().get_context_data(*args, **kwargs)
        context['time_schedule'] = mark_safe(
            time_schedule.format_schedule(schedules)
        )
        context['sum_pre'] = mark_safe(
            sum_pre['predict_pomodoro__sum']
        )
        context['sum_true'] = mark_safe(
            sum_true['true_pomodoro__sum']
        )
        context['sum_count'] = mark_safe(
            sum_count
        )
        return context

   
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'index.html'
    model = TodoModel
    fields = ('titile','author_pk','priority','start_time','end_time','predict_pomodoro','true_pomodoro')
    success_url = reverse_lazy('list') 

    def get_context_data(self, *args, **kwargs):
        user = self.request.user.pk
        todomodel = TodoModel.objects.filter(author_pk=user)
        schedules = todomodel.order_by('start_time')
        time_schedule = TimeScheduleBS4(step=10, minute_height=0.5)
        context = super().get_context_data(*args, **kwargs)
        context['time_schedule'] = mark_safe(
            time_schedule.format_schedule(schedules)
        )
        return context

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model= TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model= TodoModel
    fields = ('titile','priority')
    success_url = reverse_lazy('list')


def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return redirect('login')

    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')

