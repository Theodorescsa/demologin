from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate, login


# Create your views here.

class SiteLoginView(LoginView):
    template_name='login.html'

class SiteRegisterView(FormView):
    template_name='register.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
        username=data['username'],
        password=data['password1'],
    )
        return redirect('dangkithanhcong')


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        fieldds_classes = {'username': UsernameField}

class SiteRegisterOkView(TemplateView):
    template_name = 'dangkithanhcong.html'



class ViewUser(View):
   def get(self, request):
       if not request.user.is_authenticated:
           return HttpResponse('Đăng nhập đĩ đã')
       else: 
           return render(request,'profile.html')

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name='profile.html'