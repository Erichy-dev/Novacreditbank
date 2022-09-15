from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),





    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('services', views.services, name = 'services'),


    path('portfolio', views.portfolio, name = 'portfolio'),
    path('index', views.index, name = 'index'),
    path('transfer', views.transfer, name = 'transfer'),
    path('history', views.history, name = 'history'),
    path('loginss', views.loginss, name = 'loginss'),
    path('account', views.account, name = 'account'),
    path('realAccount', views.realAccount, name = 'realAccount'),

]
