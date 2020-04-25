from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .lib import TimeScheduleBS4

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel
    #user = User.objects.get(username = self.request.user)



class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'index.html'
    model = TodoModel
    fields = ('titile','author','author_pk','memo','priority','duedate','start_time','end_time')
    success_url = reverse_lazy('list')

    def get_context_data(self, *args, **kwargs):
        schedules = TodoModel.objects.order_by('start_time')
        time_schedule = TimeScheduleBS4(step=10, minute_height=0.5)
        context = super().get_context_data(*args, **kwargs)
        # テンプレートにhtmlを含んだ文字列を渡すときは、mark_safeをしておけばよい
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
    fields = ('titile','memo','priority','duedate')
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
            return render(request, 'list.html', {'some':100})
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            # global login_user
            # login_user = username2
            # print(login_user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logoutfunc(request):
    logout(request)
    return redirect('login')

