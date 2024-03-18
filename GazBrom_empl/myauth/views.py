from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class RegisterView(CreateView): #форма регистрации пользователя
    form_class = UserCreationForm #создать пользователя такого типа
    template_name = 'myauth/register.html' #указание шаблона
    success_url = reverse_lazy("employeesapp:employees_list") #редирект на список работников

    def form_valid(self, form): #переопределение метода, чтоб после создания пользователя проходила аутентификация
        response = super().form_valid(form) #подготовка ответа, пользователь сохранен, публикация формы
        username = form.cleaned_data.get('username') #получение из формы username
        password = form.cleaned_data.get('password1') #получение из формы password
        user = authenticate(self.request, username=username, password=password)  # получили аутентифицированного пользователя
        login(request=self.request, user=user)
        return response

def logout_view(request:HttpRequest):
    logout(request)
    return redirect(reverse("myauth:login")) #revers работает только внутри view функций
