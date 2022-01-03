from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        
        # hello_world_input 이라는 name의 값을 가져와 temp에 저장
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # accountapp 내부의 hello_world로 재접속 하라는 의미
        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # app_name:name of urlpatterns
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')    # reverse와의 차이점 : 함수에서와 클래스에서의 호출 차이
    template_name = 'accountapp/create.html'