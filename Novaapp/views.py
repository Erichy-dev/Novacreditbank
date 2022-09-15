from django.shortcuts import render
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Data
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
import webbrowser
from urllib.request import urlopen

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


# the csrf exempt doesn't pose a threat as far as you've set the CORS_ALLOW_ORIGIN variable in settings.py
@csrf_exempt
def account(request):
    # return redirect("realAccount")

    # this is should be a short-term fix. I think the problem is with the third party tools that you've used in this project.
    # they are also the reason the form's submit event has been disabled
    # plus webbrowser seems to have no support forcefully opening the link in the same tab.
    webbrowser.open("http://localhost:8000/realAccount", new=0)

def realAccount(request):
    return render(request, "account.html")
