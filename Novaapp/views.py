from django.shortcuts import render
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Data
from django.contrib.auth.mixins import LoginRequiredMixin
from Novaapp.forms import PortfolioForm
from Novaapp.models import Portfolio
from django.views.generic import TemplateView, ListView, CreateView,  UpdateView, DetailView

# Create your views here.
def home(request):

    return render(request, 'home.html', )

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')



       




@login_required
def portfolio(request):

    datas = Data.objects.all()
   
    return render(request, 'portfolio.html', {'datas' : datas})

def transfer(request):
    return render(request, 'transfer.html')

def history(request):
    return render(request, 'history.html')

def loginss(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username = username, password= password)

            if user is not None:
                auth.login(request,user)
                return redirect('portfolio')
            else:
                messages.info(request, 'Credentials Invalid')
                return redirect('loginss')
        return render(request, 'loginss.html')

def logout(request):
    auth.logout(request)
    return redirect('loginss')


class personal_info(LoginRequiredMixin, CreateView):
    login_url = '/signin/'
    form_class = PortfolioForm
    model = Portfolio
    context_name = "form"
    template_name = 'personal.html'

    def form_valid(self, form):
        obj = form.save(commit=True)
        obj.username = self.request.user
        obj.save()
        return redirect('account.html')

class UpdatePersonal_info(LoginRequiredMixin, UpdateView):
    login_url = '/signin/'
    form_class = PortfolioForm
    model = Portfolio
    context_name = "form"
    template_name = 'personal.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.username = self.request.user
        obj.save()
        return redirect('account.html')

def account(request):
    return render(request, 'account.html')






